# getTopWindow

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getTopWindow

```TypeScript
function getTopWindow(callback: AsyncCallback<Window>): void
```

获取当前应用内最后显示的窗口，使用callback异步回调。

> **说明：**&gt;
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [getLastWindow()](arkts-arkui-window-getlastwindow-f.md)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext, callback: AsyncCallback&lt;Window&gt;)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | 是 |


## getTopWindow

```TypeScript
function getTopWindow(): Promise<Window>
```

获取当前应用内最后显示的窗口，使用Promise异步回调。

> **说明：**&gt;
> 从API version 6开始支持，从API version 9开始废弃，建议使用[getLastWindow()](arkts-arkui-window-getlastwindow-f.md)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## getTopWindow

```TypeScript
function getTopWindow(ctx: BaseContext): Promise<Window>
```

获取当前应用内最后显示的窗口，使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getLastWindow()](arkts-arkui-window-getlastwindow-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## getTopWindow

```TypeScript
function getTopWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void
```

获取当前应用内最后显示的窗口，使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，参数ctx传入null或undefined时，可能会导致callback无法得到执行，建议使用
> [getLastWindow()](arkts-arkui-window-getlastwindow-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext, callback: AsyncCallback&lt;Window&gt;)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | 是 |
