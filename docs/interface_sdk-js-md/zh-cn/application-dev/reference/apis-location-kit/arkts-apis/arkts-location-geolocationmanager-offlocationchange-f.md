# offLocationChange

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationChange

```TypeScript
function offLocationChange(callback?: Callback<Location>): void
```

关闭位置变化订阅，并删除对应的定位请求。当传入的callback与onLocationChange接口传入的callback不一致时会抛出401错误码。

**起始版本：** 26.0.0

**需要权限：** 
- API版本23 - 24：ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** 
- API版本23+：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
