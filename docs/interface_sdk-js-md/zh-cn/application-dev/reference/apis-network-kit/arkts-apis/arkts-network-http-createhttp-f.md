# createHttp

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## createHttp

```TypeScript
function createHttp(): HttpRequest
```

Creates an HTTP request task.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-http-function createHttp(): HttpRequest--><!--Device-http-function createHttp(): HttpRequest-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HttpRequest](arkts-network-http-httprequest-i.md) | the HttpRequest of the createHttp. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
```

