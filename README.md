# Call Log Evaluator

Simple Python script for evaluating phone call logs in XML format.

## Context

The app [SMS Backup & Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore) exports an Android phone's call log to an XML file in the following format:

```
<calls>
  <call number="..." duration="..." date="..." ...>
  <call number="..." duration="..." date="..." ...>
</calls>
```

Any additional elements and attributes are ignored.

## The script

`process_calls.py` takes an arbitrary number of files as arguments, parses them (expecting the aforementioned format), eliminates duplicates and performs some evaluation.

Currently, the script simply calculates the number of seconds spent in calls per month.

