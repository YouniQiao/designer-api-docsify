# sendCommand

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## sendCommand

```TypeScript
function sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void
```

给位置服务子系统的各个部件发送扩展命令。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## sendCommand

```TypeScript
function sendCommand(command: LocationCommand): Promise<boolean>
```

给位置服务子系统的各个部件发送扩展命令。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md)

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
