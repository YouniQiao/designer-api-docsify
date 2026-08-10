# MediaQueryListener

媒体查询的句柄，并包含了申请句柄时的首次查询结果。媒体查询根据设置的条件语句，比如'(width <= 600vp)'，比较系统信息，若首次查询时相关信息未初始化，matches返回false。

继承自[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)。

**Inheritance/Implementation:** MediaQueryListener extends [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-mediaquery-export interface MediaQueryListener extends MediaQueryResult--><!--Device-mediaquery-export interface MediaQueryListener extends MediaQueryResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { mediaquery } from 'kits/@kit.ArkUI';
```

## offChange

```TypeScript
offChange(callback?: Callback<MediaQueryResult>): void
```

通过句柄向对应的查询条件取消注册回调，当媒体属性发生变更时不再触发指定的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQueryListener-offChange(callback?: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-offChange(callback?: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaQueryResult&gt; | No |  |

## onChange

```TypeScript
onChange(callback: Callback<MediaQueryResult>): void
```

通过句柄向对应的查询条件注册回调，当媒体属性发生变更时会触发该回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQueryListener-onChange(callback: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-onChange(callback: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaQueryResult&gt; | Yes |  |

