# DataShareUpdate (System API)

Defines the parameter information used to update the database.

The data provider needs to set the ID, read/write permissions, and basic information of the table to be shared under **proxyData** in the **module.json5** file. For details about the configuration method, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface DataShareUpdate--><!--Device-reminderAgentManager-interface DataShareUpdate-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

## equalTo

```TypeScript
equalTo: Record<string, double | string | boolean>
```

Filter criteria. Currently, only **equalTo** is supported.

**Type:** Record&lt;string, double \| string \| boolean&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataShareUpdate-equalTo: Record<string, double | string | boolean>--><!--Device-DataShareUpdate-equalTo: Record<string, double | string | boolean>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

URI of the data, which is the unique identifier for cross-application data access.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataShareUpdate-uri: string--><!--Device-DataShareUpdate-uri: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

## value

```TypeScript
value: ValuesBucket
```

New data.

**Type:** ValuesBucket

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataShareUpdate-value: ValuesBucket--><!--Device-DataShareUpdate-value: ValuesBucket-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

