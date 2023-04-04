import streamlit as st

temp = st.text_input(label='Temp',placeholder='temp')
st.header("hello")
st.text(temp)



lst = ["ID",
"SOURCESYSTEM",
"SOURCETYPE",
"SOURCE",
"TASK_NAME",
"TASK_GROUP",
"CODE_FILE",
"DEDUPE_TYPE",
"DEDUPE_OUTPUT_FILE",
"CONFIG",
"PRIMARY_SOURCE_DATABASE_NAME",
"PRIMARY_SOURCE_SCHEMA_NAME",
"PRIMARY_SOURCE_TABLE_NAME",
"DESTINATION_DATABASE_NAME",
"DESTINATION_SCHEMA_NAME",
"DESTINATION_TABLE_NAME",
"CONTAINER_NAME",
"DIRECTORY_NAME",
"LOADTYPE",
"FLAG",
"RUNTYPEFLAG",
"LASTRUNDATE",
"INSERTED_DATE",
"INSERTED_BY",
"UPDATED_BY",
"TEMP_STATUES_CHECK"]
#st.text('ID')
ID=st.text_input(label='ID',placeholder='ID')



#st.text('SOURCESYSTEM')
SOURCESYSTEM=st.text_input(label='SOURCESYSTEM',placeholder='SOURCESYSTEM')



#st.text('SOURCETYPE')
SOURCETYPE=st.text_input(label='SOURCETYPE',placeholder='SOURCETYPE')



#st.text('SOURCE')
SOURCE=st.text_input(label='SOURCE',placeholder='SOURCE')



#st.text('TASK_NAME')
TASK_NAME=st.text_input(label='TASK_NAME',placeholder='TASK_NAME')



#st.text('TASK_GROUP')
TASK_GROUP=st.text_input(label='TASK_GROUP',placeholder='TASK_GROUP')

Generated_Query = st.text("select {ID} AS ID , '{}')

#st.text('CODE_FILE')
CODE_FILE=st.text_input(label='CODE_FILE',placeholder='CODE_FILE')



#st.text('DEDUPE_TYPE')
DEDUPE_TYPE=st.text_input(label='DEDUPE_TYPE',placeholder='DEDUPE_TYPE')



#st.text('DEDUPE_OUTPUT_FILE')
DEDUPE_OUTPUT_FILE=st.text_input(label='DEDUPE_OUTPUT_FILE',placeholder='DEDUPE_OUTPUT_FILE')



#st.text('CONFIG')
CONFIG=st.text_input(label='CONFIG',placeholder='CONFIG')



#st.text('PRIMARY_SOURCE_DATABASE_NAME')
PRIMARY_SOURCE_DATABASE_NAME=st.text_input(label='PRIMARY_SOURCE_DATABASE_NAME',placeholder='PRIMARY_SOURCE_DATABASE_NAME')



#st.text('PRIMARY_SOURCE_SCHEMA_NAME')
PRIMARY_SOURCE_SCHEMA_NAME=st.text_input(label='PRIMARY_SOURCE_SCHEMA_NAME',placeholder='PRIMARY_SOURCE_SCHEMA_NAME')



#st.text('PRIMARY_SOURCE_TABLE_NAME')
PRIMARY_SOURCE_TABLE_NAME=st.text_input(label='PRIMARY_SOURCE_TABLE_NAME',placeholder='PRIMARY_SOURCE_TABLE_NAME')



#st.text('DESTINATION_DATABASE_NAME')
DESTINATION_DATABASE_NAME=st.text_input(label='DESTINATION_DATABASE_NAME',placeholder='DESTINATION_DATABASE_NAME')



#st.text('DESTINATION_SCHEMA_NAME')
DESTINATION_SCHEMA_NAME=st.text_input(label='DESTINATION_SCHEMA_NAME',placeholder='DESTINATION_SCHEMA_NAME')



#st.text('DESTINATION_TABLE_NAME')
DESTINATION_TABLE_NAME=st.text_input(label='DESTINATION_TABLE_NAME',placeholder='DESTINATION_TABLE_NAME')



#st.text('CONTAINER_NAME')
CONTAINER_NAME=st.text_input(label='CONTAINER_NAME',placeholder='CONTAINER_NAME')



#st.text('DIRECTORY_NAME')
DIRECTORY_NAME=st.text_input(label='DIRECTORY_NAME',placeholder='DIRECTORY_NAME')



#st.text('LOADTYPE')
LOADTYPE=st.text_input(label='LOADTYPE',placeholder='LOADTYPE')



#st.text('FLAG')
FLAG=st.text_input(label='FLAG',placeholder='FLAG')



#st.text('RUNTYPEFLAG')
RUNTYPEFLAG=st.text_input(label='RUNTYPEFLAG',placeholder='RUNTYPEFLAG')



#st.text('LASTRUNDATE')
LASTRUNDATE=st.text_input(label='LASTRUNDATE',placeholder='LASTRUNDATE')



#st.text('INSERTED_DATE')
INSERTED_DATE=st.text_input(label='INSERTED_DATE',placeholder='INSERTED_DATE')



#st.text('INSERTED_BY')
INSERTED_BY=st.text_input(label='INSERTED_BY',placeholder='INSERTED_BY')



#st.text('UPDATED_BY')
UPDATED_BY=st.text_input(label='UPDATED_BY',placeholder='UPDATED_BY')



#st.text('TEMP_STATUES_CHECK')
TEMP_STATUES_CHECK=st.text_input(label='TEMP_STATUES_CHECK',placeholder='TEMP_STATUES_CHECK')

for i in range(0,len(lst)):
    if i == 0:
        print(f"select {lst[i]} AS {lst[i]},")
    else:
        print(f"'{lst[i]}' AS {lst[i]},")
