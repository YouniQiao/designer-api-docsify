# replace

## 导入模块

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## replace

```TypeScript
function replace(options: RouterOptions): void
```

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](../../../ui/arkts-navigation-architecture.md)。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)(options: router.RouterOptions)

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | 是 |
