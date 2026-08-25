# sendCommand

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## sendCommand

```TypeScript
function sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void
```

给位置服务子系统的各个部件发送扩展命令。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |


## sendCommand

```TypeScript
function sendCommand(command: LocationCommand): Promise<void>
```

给位置服务子系统的各个部件发送扩展命令。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
