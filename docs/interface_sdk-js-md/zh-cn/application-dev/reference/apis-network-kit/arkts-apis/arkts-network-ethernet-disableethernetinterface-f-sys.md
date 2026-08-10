# disableEthernetInterface（系统接口）

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## disableEthernetInterface

```TypeScript
function disableEthernetInterface(): Promise<void>
```

Disable the ethernet interface.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ethernet-function disableEthernetInterface(): Promise<void>--><!--Device-ethernet-function disableEthernetInterface(): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned when the ethernet interface is disabled. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

