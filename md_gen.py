from pydantic.dataclasses import dataclass



@dataclass(frozen=True)
class MDTableDescription:
    table_name: str
    table_schema: str | None
    table_comment: str | None

@dataclass(frozen=True)
class MDColumnDescription:
    column_name: str
    column_comment: str | None
    column_type: str
    column_nullable: bool
    column_primary_key: bool
    #column_foreign_key: str
    

class MDGen:
    def __init__(self, mapper):
        self.mapper = mapper
        self.descriptions = []
        self.main()
        
    def main(self):
        for mapper in self.mapper.mappers:
            table_info = self.gen_table_info(mapper)
            columns_info = self.gen_columns_info(mapper)
            self.add_to_descriptions(table_info, columns_info)

    def gen_table_info(self, mapper):
        tab_descr = MDTableDescription(
            table_schema = mapper.local_table.schema,
            table_name = mapper.local_table.name,
            table_comment = mapper.local_table.comment
        )
        return tab_descr

    def gen_columns_info(self, mapper):
        cols = []
        for column in mapper.local_table.columns._all_columns:
            col_desc = MDColumnDescription(
                column_name=column.name,
                column_comment = column.comment,
                column_type = str(column.type),
                column_nullable = column.nullable,
                column_primary_key = column.primary_key
                )
            cols.append(col_desc)
        return cols

    def get_foreign_keys(self, column):
        for fk in column.foreign_keys:
            print(fk)

    def add_to_descriptions(
        self, 
        table_info: MDTableDescription, 
        columns_info: MDColumnDescription):
        self.descriptions.append({"table":table_info, "columns":columns_info})

    def generate(self):
        from utils.md_gen import markdowngenerator as mg

        with mg.MarkdownGenerator(
            filename='readme.md', enable_write=False, syntax='GitLab'
        ) as doc:
            doc.addHeader(1, "Hello there!")
            doc.writeTextLine(f'{doc.addBoldedText("This is just a test.")}')
            doc.addHeader(2, "Second level header.")
            # table = [
            #     {"Column": "col1row1 data", "Column2": "col2row1 data"},
            #     {"Column1": "col1row2 data", "Column2": "col2row2 data"},
            # ]

            doc.addTable(html_escape=True,header_names=['h1','h2','3'], row_elements=[['d1','d2','d3'],['d1','d2','d3']])
            doc.writeTextLine("Ending the document....")

        

