# TriggerCondition

Defines the triggering condition parameters of the **onTrigger** callback of a [Watcher]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface TriggerCondition--><!--Device-hiAppEvent-interface TriggerCondition-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## row

```TypeScript
row?: int
```

Total number of events that trigger callback. The value is a positive integer. The default value is 0, indicating that no callback is triggered. If this parameter is set to a negative value, the default value is used.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TriggerCondition-row?: int--><!--Device-TriggerCondition-row?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## size

```TypeScript
size?: int
```

Total size of events that trigger callback. The value is a positive integer, in bytes. The default value is 0,indicating that no callback is triggered. If this parameter is set to a negative value, the default value is used.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TriggerCondition-size?: int--><!--Device-TriggerCondition-size?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## timeOut

```TypeScript
timeOut?: int
```

Timeout interval for triggering callback. The value is a positive integer, in unit of 30s. The default value is0, indicating that no callback is triggered. If this parameter is set to a negative value, the default value is used.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TriggerCondition-timeOut?: int--><!--Device-TriggerCondition-timeOut?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

