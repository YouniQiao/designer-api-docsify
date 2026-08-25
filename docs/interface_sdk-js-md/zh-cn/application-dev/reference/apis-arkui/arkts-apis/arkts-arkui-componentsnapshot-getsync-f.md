# getSync

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## getSync

```TypeScript
function getSync(id: string, options?: SnapshotOptions): image.PixelMap
```

获取已加载的组件的截图，传入组件的组件标识，找到对应组件进行截图。同步等待截图完成返回[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)。

> **说明：**&gt;
> 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**起始版本：** 12

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
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [160002](../errorcode-snapshot.md#160002-截图超时) |
| [160003](../errorcode-snapshot.md#160003-截图选项中设置的色彩空间或动态范围模式不受支持) |
