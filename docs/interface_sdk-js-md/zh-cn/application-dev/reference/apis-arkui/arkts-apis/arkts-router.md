# @ohos.router

Router提供页面跳转能力，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。推荐使用[Navigation组件](../../../ui/arkts-navigation-architecture.md)作为应用路由框架。

> **说明：**&gt;
> - 页面路由需要在页面渲染完成之后才能调用，在onInit和onReady生命周期中页面还处于渲染阶段，禁止调用页面路由方法。&gt;
> - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)说明。&gt;
> - 如果使用传入callback形式的
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)
> 或
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)
> 接口，callback中通过[getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength)等接口获取的栈信息为中间态的栈信息，可能与栈操作完全结束后，再通过
> [getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength)等接口获取的栈信息不一致。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { router } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [back](arkts-arkui-router-back-f.md) |
| [back](arkts-arkui-router-back-f.md) |
| [clear](arkts-arkui-router-clear-f.md) |
| [disableAlertBeforeBackPage](arkts-arkui-router-disablealertbeforebackpage-f.md) |
| [enableAlertBeforeBackPage](arkts-arkui-router-enablealertbeforebackpage-f.md) |
| [getLength](arkts-arkui-router-getlength-f.md) |
| [getParams](arkts-arkui-router-getparams-f.md) |
| [getState](arkts-arkui-router-getstate-f.md) |
| [getStateByIndex](arkts-arkui-router-getstatebyindex-f.md) |
| [getStateByUrl](arkts-arkui-router-getstatebyurl-f.md) |
| [hideAlertBeforeBackPage](arkts-arkui-router-hidealertbeforebackpage-f.md) |
| [push](arkts-arkui-router-push-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [replace](arkts-arkui-router-replace-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [showAlertBeforeBackPage](arkts-arkui-router-showalertbeforebackpage-f.md) |

### 接口

| 名称 |
| --- |
| [EnableAlertOptions](arkts-arkui-router-enablealertoptions-i.md) |
| [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) |
| [RouterOptions](arkts-arkui-router-routeroptions-i.md) |
| [RouterState](arkts-arkui-router-routerstate-i.md) |

### 枚举

| 名称 |
| --- |
| [RouterMode](arkts-arkui-router-routermode-e.md) |
