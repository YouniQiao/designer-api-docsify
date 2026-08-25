# createFromBuilder

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## createFromBuilder

```TypeScript
function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,
    delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void
```

在应用后台渲染CustomBuilder自定义组件，并输出其截图。通过回调返回结果并支持在回调中获取离屏组件绘制区域坐标和大小。

> **说明：**&gt;
> - 从API version 12开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)方法
> 获取当前UI上下文关联的[ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)对象。&gt;
> - 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟。&gt;
> - builder中的组件不支持设置动画相关的属性，如transition。&gt;
> - 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的Image组件、Web组件。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** createFromBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |
| delay | number | 否 |
| checkImageStatus | boolean | 否 |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [160001](../errorcode-snapshot.md#160001-图像加载错误) |


## createFromBuilder

```TypeScript
function createFromBuilder(builder: CustomBuilder, delay?: number,
    checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>
```

在应用后台渲染CustomBuilder自定义组件，并输出其截图。通过Promise返回结果，支持获取离屏组件绘制区域的坐标和大小。

> **说明：**&gt;
> - 从API version 12开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentsnapshot)方法
> 获取当前UI上下文关联的[ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md)对象。&gt;
> - 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟。&gt;
> - builder中的组件不支持设置动画相关的属性，如transition。&gt;
> - 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的Image组件、Web组件。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** createFromBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 |
| delay | number | 否 |
| checkImageStatus | boolean | 否 |
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
| [160001](../errorcode-snapshot.md#160001-图像加载错误) |
