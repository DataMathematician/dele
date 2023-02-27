from pydantic.dataclasses import dataclass
from dataclasses import asdict
from devtools import debug
from pathlib import Path

@dataclass(frozen=True)
class MDColumnDescription:
    column_name: str
    column_comment: str | None
    column_type: str
    column_nullable: bool
    column_primary_key: bool
    #column_foreign_key: str

@dataclass(frozen=True)
class MDDescription:
    #table_path: str
    #md_header: str | None

    table_name: str
    table_schema: str | None
    table_comment: str | None
    table_columns: list[MDColumnDescription]
    table_path: str
    table_source: str | None
    table_entity: str | None

    

class MDGen:
    def __init__(self, mapper):
        self.mapper = mapper
        self.descriptions = []
        self.main()
        
    def main(self):
        for mapper in self.mapper.mappers:
            md_description = self.gen_md_description(mapper)
            self.add_to_descriptions(md_description)

    def gen_md_description(self, mapper):
        return MDDescription(
            table_schema = mapper.local_table.schema,
            table_name = mapper.local_table.name,
            table_comment = mapper.local_table.comment,
            table_columns = self.gen_columns(mapper.columns),
            table_path = self.get_dataclass_path(),
            
            table_source = self.get_source(mapper.columns),
            table_entity = self.get_entity(mapper.columns),
            
        )

    def get_dataclass_path(self) -> Path:
        """return Path
        """
        return str(Path(__file__).parent / "descriptions")

    def get_source(self, columns):
        kw = 'source'
        for column in columns._all_columns:
            if column.default is not None and column.name == kw:
                default = column.default.arg
                return default
        
        return None

    def get_entity(self, columns):
        kw = 'entity'
        for column in columns._all_columns:
            if column.default is not None and column.name == kw:
                default = column.default.arg
                return default
        
        return None

    def gen_columns(self, columns):
        cols = []
        for column in columns._all_columns:
            col = MDColumnDescription(
                column_name=column.name,
                column_comment = column.comment,
                column_type = str(column.type),
                column_nullable = column.nullable,
                column_primary_key = column.primary_key                
            )
            cols.append(col)
        return cols


            #table_entity = mapper.columns,
            #md_header = mapper

    # def gen_table_info(self, mapper):
    #     tab_descr = MDDescription(
    #         table_schema = mapper.local_table.schema,
    #         table_name = mapper.local_table.name,
    #         table_comment = mapper.local_table.comment
    #         table_entity= = mapper.columns
    #     )
    #     return tab_descr

    # def gen_columns_info(self, mapper):
    #     cols = []
    #     for column in mapper.local_table.columns._all_columns:
    #         col_desc = MDColumnDescription(
    #             column_name=column.name,
    #             column_comment = column.comment,
    #             column_type = str(column.type),
    #             column_nullable = column.nullable,
    #             column_primary_key = column.primary_key
    #             )
    #         cols.append(col_desc)
    #     return cols

    # def get_foreign_keys(self, column):
    #     for fk in column.foreign_keys:
    #         print(fk)

    def add_to_descriptions(self, md_description: MDDescription):
        self.descriptions.append(md_description)

    def generate_table(self, description):
        q = []
        for col in description.table_columns:
            dic = {k: str(v) for k, v in asdict(col).items()}
            q.append(dic)
        return q
        

    def generate(self):
        from utils.md_gen import markdowngenerator as mg

        for description in self.descriptions:
            with mg.MarkdownGenerator(
                filename=description.table_path + f"/{'' if description.table_schema is None else description.table_schema + '_'}{description.table_name}.md", 
                enable_write=False,
                encoding='utf-8',
                enable_TOC=False
            ) as doc:
                doc.addHeader(2, f"Описание")
                doc.addTable(
                    html_escape=True,
                    dictionary_list=[
                        {
                            "Источник":f"{description.table_source}",
                            "Схема MDM":f"{description.table_schema}",
                            "Имя таблицы MDM":f"{description.table_name}",
                            "Сущность":f"{description.table_entity}",
                            "Комментарий":f"{description.table_comment}"
                        }
                    ],
                )
                doc.addHeader(2, f"dataclass")
                doc.writeTextLine(f'{doc.addBoldedText("Описание объекта")}')
                doc.addTable(
                    html_escape=True,
                    dictionary_list=self.generate_table(description)
                )
                doc.writeTextLine("Ending the document....")

        

