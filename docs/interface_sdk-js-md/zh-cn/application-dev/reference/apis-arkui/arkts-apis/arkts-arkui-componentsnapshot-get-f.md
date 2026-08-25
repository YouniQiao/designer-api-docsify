# get

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## get

```TypeScript
function get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void
```

获取已加载的组件的截图，传入组件的组件标识，找到对应组件进行截图。通过回调返回结果。

> **说明：**&gt;
> - 从API version 12开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)方法
> 获取当前UI上下文关联的[ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)对象。&gt;
> - 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** get

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |


## get

```TypeScript
function get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>
```

获取已加载的组件的截图，传入组件的组件标识，找到对应组件进行截图。通过Promise返回结果。

> **说明：**&gt;
> - 从API version 12开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)方法
> 获取当前UI上下文关联的[ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)对象。&gt;
> - 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** get

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
