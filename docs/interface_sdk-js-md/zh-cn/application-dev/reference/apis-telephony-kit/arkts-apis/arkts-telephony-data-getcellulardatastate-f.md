# getCellularDataState

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## getCellularDataState

```TypeScript
function getCellularDataState(callback: AsyncCallback<DataConnectState>): void
```

Obtain the connection state of the PS domain.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function getCellularDataState(callback: AsyncCallback<DataConnectState>): void--><!--Device-data-function getCellularDataState(callback: AsyncCallback<DataConnectState>): void-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataConnectState&gt; | 是 | Indicates the callback for getting the connection state, which can be any of the following: &lt;ul&gt; &lt;li&gt;{@code DataConnectState#DATA_STATE_UNKNOWN} &lt;li&gt;{@code DataConnectState#DATA_STATE_DISCONNECTED} &lt;li&gt;{@code DataConnectState#DATA_STATE_CONNECTING} &lt;li&gt;{@code DataConnectState#DATA_STATE_CONNECTED} &lt;li&gt;{@code DataConnectState#DATA_STATE_SUSPENDED} &lt;/ul&gt; |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

## 示例

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState((err: BusinessError, contextData: data.DataConnectState) => {
    if(err) {
        console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`getCellularDataState success`);
    }
});
```


## getCellularDataState

```TypeScript
function getCellularDataState(): Promise<DataConnectState>
```

Obtain the connection state of the PS domain.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function getCellularDataState(): Promise<DataConnectState>--><!--Device-data-function getCellularDataState(): Promise<DataConnectState>-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;DataConnectState&gt; | Returns the connection state, which can be any of the following: &lt;ul&gt; &lt;li&gt;{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

## 示例

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState().then((contextData: data.DataConnectState) => {
    console.info(`getCellularDataState success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}`);
});
```

