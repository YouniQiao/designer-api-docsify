# AppEventPackage

Defines parameters of an **AppEventPackage** object. This API is used to obtain detail information about an event package, which is obtained using the [takeNext]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface AppEventPackage--><!--Device-hiAppEvent-interface AppEventPackage-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## appEventInfos

```TypeScript
appEventInfos: Array<AppEventInfo>
```

Event object group.

**Atomic service API**: This parameter can be used in atomic services since API version 12.

**Type:** Array&lt;AppEventInfo&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppEventPackage-appEventInfos: Array<AppEventInfo>--><!--Device-AppEventPackage-appEventInfos: Array<AppEventInfo>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## data

```TypeScript
data: string[]
```

Event data in the event package.

**Atomic service API**: This parameter can be used in atomic services since API version 11.

**Type:** string[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-data: string[]--><!--Device-AppEventPackage-data: string[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## packageId

```TypeScript
packageId: int
```

Event package ID, which is named from **0** in ascending order.

**Atomic service API**: This parameter can be used in atomic services since API version 11.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-packageId: int--><!--Device-AppEventPackage-packageId: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## row

```TypeScript
row: int
```

Number of events in the event package.

**Atomic service API**: This parameter can be used in atomic services since API version 11.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-row: int--><!--Device-AppEventPackage-row: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## size

```TypeScript
size: int
```

Event size of the event package, in bytes.

**Atomic service API**: This parameter can be used in atomic services since API version 11.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-size: int--><!--Device-AppEventPackage-size: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

