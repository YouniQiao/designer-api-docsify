# AppEventPackage

提供订阅返回的事件包的参数定义。可用于获取事件包的详细信息，事件包由[takeNext](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md#takenext)接口获得。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface AppEventPackage--><!--Device-hiAppEvent-interface AppEventPackage-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## appEventInfos

```TypeScript
appEventInfos: Array<AppEventInfo>
```

事件对象集合。

**原子化服务API：** 从API version 12开始，该参数支持在原子化服务中使用。

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

事件包的事件信息。

**原子化服务API：** 从API version 11开始，该参数支持在原子化服务中使用。

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

事件包ID，从0开始自动递增。

**原子化服务API：** 从API version 11开始，该参数支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-packageId: int--><!--Device-AppEventPackage-packageId: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## row

```TypeScript
row: int
```

事件包的事件数量。

**原子化服务API：** 从API version 11开始，该参数支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-row: int--><!--Device-AppEventPackage-row: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## size

```TypeScript
size: int
```

事件包的事件大小，单位为byte。

**原子化服务API：** 从API version 11开始，该参数支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackage-size: int--><!--Device-AppEventPackage-size: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

