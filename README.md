# khd_voucherDataProcessingScript
Python script to crosswalk and reformat template voucher data into DarwinCore for import into Symbiota. Script written by Ernie Marx & Richard Levy.

See TEMPLATE_herbariumVoucherData.xslx for data input template.

Usage for mode 2 (using IDE): Move the .xlsx or .csv file containing data provided by field collector into the workspace directory. Open the KHD_voucher_data_script.py file and change the paths on lines 49 and 50 to reflect the original data file and the output file. Run the script and the new proccessed file will be created at the specified path.

Script will concatenate and format fields from template CSV into DarwinCore. Template and script are written to follow Kathryn Kalmbach Herbarium data collection and processing practices.

## Summary of processes ##

* Fields from template describing habitat (habitatType, microhabitat, landuse/disturbance, slope, aspect, terrain, additional habitat descriptions) are formatted and concatenated into 'habitat' field.

* Data from field 'Permit' is formatted and placed into 'dataGeneralizations.

* Fields from template considered notes (Project Title, Frequency, Tissue Collected, additionalCollectorNotes, iNaturalist ID) formatted and concatenated into 'occurrenceRemarks' field.

* Fields from template describing organism (habit, graminoidHabit, lifeCycleHabit, flowerColor, heightInCentimeters, additionalDescription) formatted and concatenated into 'description' field (Symbiota, not DwC).

* Fields from template describing organism (habit, graminoidHabit, lifeCycleHabit, flowerColor, heightInCentimeters, additionalDescription) formatted as JSON and concatenated into 'dynamicProperties' field. Secondary manual manipulation may be required for "additionalDescription" values.

* materialSample_sampleType, materialSample_disposition, materialSample_preservationType populated based upon values provided by user in "Tissue Collected" field. For use in Symbiota Portals with materialSample module.

* establishmentMeans field populated based upon values provided by user in "cultivationStatus".

* Elevation values retrieved from USGS Bulk Point Query Service (V 2.0) API using decimalLatitude and decimalLongitude values provided by user and populated in minimumElevationInMeters_2 field (so as not to overwrite any provided elevation values). A note about the source of the elevation value is populated in "georeferenceRemarks". 
