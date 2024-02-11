# Fractured Data Mininer
**NOTE: Tool is not in a usable state yet.**

## What does it do/will do?
The tool will be used to extract data from Fracrued Online Decompiled Assets [^1] . This data will be stored in a database
for further use.
[^1]: The assets are comiled by Unity, so tools need to be used to decomplile them into plain text.

## Minimal Viable Product Features
- [ ] Parse Item data and put the in SQLite Database
    - [ ] Name - Formating needs to be done
    - [ ] Type - is defined by id
    - [ ] Description 
    - [ ] Icon or a link to it

- [ ] Regent Item
    - [ ] Aspect Type
    - [ ] Aspect Values

## Other Future Featurs
- [ ] Monster Data
    - [ ] Name
    - [ ] Type
    - [ ] Weakness
    - [ ] Drop Table - This will need some id linking
    - [ ] Know Locations - This will be gatherd from users, since its not stored in the game files
- [ ] Spell Data
    - [ ] Name
    - [ ] Type
    - [ ] Cost
    - [ ] Effect
- [ ] Other Useful Data I find in the files
