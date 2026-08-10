# @ohos.mediaquery

提供根据不同媒体类型定义不同的样式。

> **说明：**
> 
> - 以下API需先使用UIContext中的[getMediaQuery()](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmediaquery)方法
> 获取到MediaQuery对象，再通过该对象调用对应方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace mediaquery--><!--Device-unnamed-declare namespace mediaquery-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { mediaquery } from 'kits/@kit.ArkUI';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [MediaQueryListener](arkts-arkui-mediaquery-mediaquerylistener-i.md) | 媒体查询的句柄，并包含了申请句柄时的首次查询结果。媒体查询根据设置的条件语句，比如'(width <= 600vp)'，比较系统信息，若首次查询时相关信息未初始化，matches返回false。  继承自[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)。 |
| [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md) | 用于执行媒体查询操作。 |

