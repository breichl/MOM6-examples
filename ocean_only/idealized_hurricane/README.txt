To run with waves:

ThisDirectory=pwd (running/working dir)

copy grid_spec.nc to ThisDirectory/INPUT
copy StkSpec.nc to ThisDirectory

copy data_table_WAVES to data_table
copy diag_table_WAVES to diag_table
copy MOM_override_WAVES to MOM_override

This enables the waves module and some outputs.  It does not affect the model solution.
