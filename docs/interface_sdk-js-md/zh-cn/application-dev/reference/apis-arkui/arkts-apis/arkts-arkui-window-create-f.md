# create

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(id: string, type: WindowType, callback: AsyncCallback<Window>): void
```

创建子窗口，使用callback异步回调。子窗口创建后默认是[沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，参数id传入null或undefined时，可能会导致callback无法得到执行，建议使用
> [createWindow()](arkts-arkui-window-createwindow-f.md)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration, callback: AsyncCallback&lt;Window&gt;)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | 是 |


## create

```TypeScript
function create(id: string, type: WindowType): Promise<Window>
```

创建子窗口，使用Promise异步回调。子窗口创建后默认是[沉浸式布局](../../../windowmanager/window-terminology.md#沉浸式布局)。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用[createWindow()](arkts-arkui-window-createwindow-f.md)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## create

```TypeScript
function create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>
```

创建系统窗口，使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[createWindow()](arkts-arkui-window-createwindow-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| id | string | 是 |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## create

```TypeScript
function create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void
```

创建系统窗口，使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [createWindow()](arkts-arkui-window-createwindow-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration, callback: AsyncCallback&lt;Window&gt;)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| id | string | 是 |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | 是 |
