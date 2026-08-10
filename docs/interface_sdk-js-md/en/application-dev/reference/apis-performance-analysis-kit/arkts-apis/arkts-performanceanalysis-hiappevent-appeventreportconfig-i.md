# AppEventReportConfig

数据处理者可以上报事件的描述配置。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface AppEventReportConfig--><!--Device-hiAppEvent-interface AppEventReportConfig-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## domain

```TypeScript
domain?: string
```

事件领域。默认为空字符串，事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventReportConfig-domain?: string--><!--Device-AppEventReportConfig-domain?: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## isRealTime

```TypeScript
isRealTime?: boolean
```

是否实时上报事件。默认值为false，配置值为true表示实时上报事件，false表示不实时上报事件。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventReportConfig-isRealTime?: boolean--><!--Device-AppEventReportConfig-isRealTime?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## name

```TypeScript
name?: string
```

事件名称。默认为空字符串，首字符必须为字母字符或\$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventReportConfig-name?: string--><!--Device-AppEventReportConfig-name?: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

