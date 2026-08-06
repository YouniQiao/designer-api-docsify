# Template

Defines the struct of the template used in a subscription.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface Template--><!--Device-dataShare-interface Template-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## predicates

```TypeScript
predicates: Record<string, string>
```

Predicates to use. When  
[**on**]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_is called, the predicates are used to generate data. This parameter applies only to RDB data storage.

**Type:** Record&lt;string, string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Template-predicates: Record<string, string>--><!--Device-Template-predicates: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## scheduler

```TypeScript
scheduler: string
```

Template scheduler SQL, which is embedded with a custom function. Currently, the **remindTimer** function is embedded. The **remindTimer** triggers a subscription-based update in specified scenarios.

The scheduler SQL statement is triggered when:

1. The subscribed data is modified.2. The first subscription is added to the corresponding database.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Template-scheduler: string--><!--Device-Template-scheduler: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## update

```TypeScript
update?: string
```

Update SQL statement of a specified template. The default value is an empty string. When  
[on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_is called, the **update** parameter is used to update data. This parameter applies only to RDB data storage.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Template-update?: string--><!--Device-Template-update?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

