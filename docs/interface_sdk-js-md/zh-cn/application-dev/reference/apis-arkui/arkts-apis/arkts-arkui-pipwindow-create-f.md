# create

## 导入模块

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: PiPConfiguration): Promise<PiPController>
```

创建画中画控制器，使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [PiPConfiguration](arkts-arkui-pipwindow-pipconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PiPController](arkts-arkui-pipwindow-pipcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |


## create

```TypeScript
function create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController>
```

创建画中画控制器，使用typeNode为画中画添加自定义UI节点。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [PiPConfiguration](arkts-arkui-pipwindow-pipconfiguration-i.md) | 是 |
| contentNode | typeNode.XComponent | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PiPController](arkts-arkui-pipwindow-pipcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
