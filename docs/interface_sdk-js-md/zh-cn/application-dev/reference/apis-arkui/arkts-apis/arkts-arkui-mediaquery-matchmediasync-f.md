# matchMediaSync

## 导入模块

```TypeScript
import { mediaquery } from 'kits/@kit.ArkUI';
```

## matchMediaSync

```TypeScript
function matchMediaSync(condition: string): MediaQueryListener
```

设置媒体查询的查询条件，并返回对应的监听句柄。

> **说明：**&gt;
> -matchMediaSync需先通过[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getMediaQuery](arkts-arkui-arkui-uicontext-uicontext-c.md#getmediaquery)方法获取
> [MediaQuery](arkts-arkui-arkui-uicontext-uicontext-c.md)对象，然后通过该对象进行调用。&gt;
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getMediaQuery](arkts-arkui-arkui-uicontext-uicontext-c.md#getmediaquery)方法获取当前UI上下文关联的
> [MediaQuery](arkts-arkui-arkui-uicontext-uicontext-c.md)对象。

**起始版本：** 7

**废弃版本：** 18

**替代接口：** matchMediaSync

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | string | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaQueryListener](arkts-arkui-mediaquery-mediaquerylistener-i.md) |
