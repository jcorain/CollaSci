# CollaSci 

## Purpose

CollaSci is a python package aimed to develop scientific collaboration via 
database management and easy visualization. At first, the database is based on 
condensed matter data related to magnetism and developing user interface 
to easily add and share data. 

## Magnetism database 

The magnetism database is written in SQLITE using python syntax and format. 
It consists of 11 different tables : 
- status
- university
- laboratory
- user
- experiment type
- experiment setup
- material type
- compound
- batch
- project
- data

Each table present a **primary key which is called id** and which is used to 
join the tables together via foreign keys. Note that for each foreign keys we 
decided to update the tables ON CASCADE, meaning that when an entry is altered 
in a tbale, the changes are directly reflected in the linked tables.

The summary of the tables and the relationship diagram can be found in 
**CollaSciTablesrelationship.pptx**

### user related tables

#### status table

The satus table is dedicated to store the different status type that someone
can have (Intern, PhD Student, Full Professor ...) and has the following columns:
- id (int) the primary key .
- name (varchar(100)) the name of the status.

Each row must present a **unique name**.

#### university table

The university table is dedicated to store the data related to each university
and has the columns : 
- id (int) the primary key.
- name (varchar(100)) the name of the university.
- country (varchar(100)) the country where the university is.
- city (varchar(100)) the city where the university sits.
- address (text) the address of the university.

Each row must present a **unique university name**. 

#### laboratory table

The laboratory table is dedicated to store the different laboratories and has
the columns : 
- id (int) the primary key.
- name (text) the name of the laboratory.
- university_id (int) the id of the universtiy affilited to the laboratory and 
present in the university table.

We assumed that each laboratory has a different name, and therefore developped
the functions in order to have a **unique laboratory name for each row**. 

In addition, as this table is linked to university id, the university table
must be cretaed prior to the laboratory one, and the related values must be
already in the database.

#### user table

The user table is dedicated to storee the data related to the user and has the
following columns:
- id (int) the primary key.
- firstname (varchar(100)) the first name of the user.
- lastname (varchar(100)) the lastname of the user.
- status_id (int) the id coming from the status table.
- laboratory_id (int) the id comming from the user laboratory.  

Taking into account that during its carreer, a reseracher is moving quite a lot, 
the function used to create a new row will check if the user already exists
for the laboratory, i.e. the table store **unique combination of firstname **
**lastname and laboratory_id**

In addition, as this table is linked to the status and laboratory id, those
tables must be created prior to the user one, and the related values must be
already in the database.

### experiment related tables

#### experiment type table
The experiment type table is dedicated to store each type of experiment 
(i.e magnetization vs Temp) that can be used and stored in the database and has
the following columns : 
- id (int) the primary key.
- name (text) the name of the experiment type.

Each row must present a **unique name**

#### experiment setup table

The experiment setup table is dedicated to store each experiemental setup that 
can be used iton the database. It has the following columns : 
- id (int) the primary key.
- name (text) the name of the experimental setup.
- room_name (text) the name of the room where the experimental setup is.
- start_date (date) the date when the experiemetal setup was set.
- min_field (real can be None) the minimum field of the setup if it exists.
- max_field (real can be None) the maximum field of the setup if it exists.
- min_temperature (real can be None) the minimum temperature if it exists.
- max_temperature (real can be None) the maximum temperature if it exists.
- experiment_type_id (int) the id related to the experiment type.
- responsible_id (int) the id related to the user responsible of the experiment.

Taking into account that ech user is already untitled to a laboratory, we
decided to not add a laboratory_id column which would have been redundant with 
the user one has the user table already present this information. 

Therefore, each row must present a **unique combination of name and responsible_id**

In addition, as this table is linked to the experiment type and user ids, those
tables must be created prior to the experiment setup one, and the related 
values must be already in the database.

### material related tables

#### material type table

The material type table is dedicated to store the different material type (i. e.
superconductor, spin liquid ...) that can be studied. It presents the following
rows : 
- id (int) the primary key.
- name (text) the name of the material type.

Each row must presents a **unique name**.

#### compound table

The compound table is dedicated to store the different compounds beeing studied.
It presents the following rows : 
- id (int) the primary key.
- name (text) the name of the compound. 
- formula (varchar(100)) the chemical formua of the compound.
- material_type_id (int) teh id related to the compound's material type.

Each row must present a **unique name**.

In addition, as this table is linked to the material type id, the material type
table must be created prior to the compound one, and the related 
values must be already in the database.

#### batch table 

The batch table is dedicated to store the data related to each compound's batch.
It presents the following rows : 
- id (int) the primary key.
- name (text) the name of the batch.
- mass (real) the mass of the batch.
- color (varchar(50)) the color of the batch
- type (varchar(50)) the cristalline type of the batch. Must be powder, 
single cristal or polycristal.
- creation_date (date) the date when the batch has been synthesized. 
- compound_id (int) the id related to the compound table.
- grower_id (int) the id related to the user who has grown the sample.

To ensure that we can compare different batchs, each row nust present a 
**unique name**.

In addition, as this table is linked to the copund and user ids, those
tables must be created prior to the batch one, and the related 
values must be already in the database.

### project table 

The project table is dedicated to store the data related to each project. For
the momemt we decided to not set too much informations into this table to keep 
it readable, therefore it only presnets the following rows : 
- id (int) the primary key.
- name (text) the name of the project.
- responsible_id (int) the id related to the responsible user.

Each row must present a **unique name**.

In addition, as this table is linked to the user id, the user
table must be created prior to the compound one, and the related 
values must be already in the database.
 
### data table

The data table is dedicated to store teh data related to the taken data. It
presents the following rows :
- id (int) the primary key.
- mass (real) the mass of the batch used for the experiment
- experiment_no (int) the number representing how many times the same experiment
has been conducted
- field (real can be None) the magnetic field used if it exists 
- temp (real can be None) the temperature set if it exists
- date (date) the date when the experiment has been conducted
- path_import (text) teh path where the experimental data has been firstly stored.
- new_path (text) the new path where the experimental data is automatically copied. 
- comment (text can be None) any comment on the experiment.
- experiment_setup_id (int) the id related to the used experimental setup.
- user_id (int) the id related to the user who performed the experiment.
- batch_id (int) the id related to the used batch.
- project_id (int) the id related to the project. 

When adding new values to the table, we decided to copy the data into a new path
and store them in a well defined way in order to easily retrieve them. 
The new path has been defined as 

app_rep/project_name/compound_name/batch_name/experiment_type_name/experiment_setup_name

and the new filename is defined as 

batch_name_experiement_type_name_experiment_setup_name_user_lastname_field(if exists)_temperature(if exists)_experiment_no_date

The stored new_path is new_path/new_filename

As the new path contains information about every aspect of the data, we decided
to store **unique value of new_path**.

In addition, as this table is linked to the experiment setup, batch, project 
and user ids, those table must be created prior to the compound one, and the 
related values must be already in the database.

## Bug reporting 

To report a bug, please use the gitlab page for the package for the sake of 
documentation. You can open a new issue on this page and we will try to tackle 
it down.

## Contribution

Any contribution is most welcomed. Feel free to contact the maintainer of the 
package for any added value.