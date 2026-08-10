# newSEService

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## newSEService

```TypeScript
function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService
```

Establish a new connection that can be used to connect to all the SEs available in the system.The connection process can be quite long, so it happens in an asynchronous way. It is usable only if the specified callback is called or if isConnected() returns true.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 12

**替代接口：** [omapi#createService](arkts-connectivity-omapi-createservice-f.md#createservice)

<!--Device-omapi-function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService--><!--Device-omapi-function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService-End-->

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'serviceState' | 是 | nfc serviceState |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ServiceState&gt; | 是 | The callback to return the service. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SEService](arkts-connectivity-omapi-seservice-i.md) | The new SEService instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |

## 示例

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    // 获取 service
    try {
        seService = omapi.newSEService("serviceState", (state) => {
        hilog.info(0x0000, 'testTag', 'se service state = %{public}s', JSON.stringify(state));
        });
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'newSEService error %{public}s', JSON.stringify(error));
    }
    if (seService == undefined || !seService.isConnected()) {
        hilog.error(0x0000, 'testTag', 'secure element service disconnected.');
        return;
    }
}
```

