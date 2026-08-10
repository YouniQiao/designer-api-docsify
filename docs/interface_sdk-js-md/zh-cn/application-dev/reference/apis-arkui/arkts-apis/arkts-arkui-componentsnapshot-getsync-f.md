# getSync

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## getSync

```TypeScript
export function getSync(id: string, options?: SnapshotOptions): image.PixelMap | null
```

Take a screenshot of the specified component in synchronous mode,this mode will block the main thread, please use it with caution, the maximum waiting time of the interface is 3s, if it does not return after 3s, an exception will be thrown.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-componentSnapshot-export function getSync(id: string, options?: SnapshotOptions): image.PixelMap | null--><!--Device-componentSnapshot-export function getSync(id: string, options?: SnapshotOptions): image.PixelMap | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | Target component ID, set by developer through .id attribute. |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | 否 | Define the snapshot options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | The snapshot result in PixelMap format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Invalid ID. |
| 160002 | Timeout. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

