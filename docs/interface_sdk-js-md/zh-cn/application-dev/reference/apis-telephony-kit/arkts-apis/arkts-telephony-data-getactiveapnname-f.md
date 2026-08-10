# getActiveApnName

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## getActiveApnName

```TypeScript
function getActiveApnName(): Promise<string>
```

Get Active APN's Name.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function getActiveApnName(): Promise<string>--><!--Device-data-function getActiveApnName(): Promise<string>-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Returns the name of the active APN or null if cellular network is not active. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

## 示例

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getActiveApnName().then((apn: string) => {
    console.info(`getActiveApnName success, apn: ${apn}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveApnName failed. code: ${err.code}, message: ${err.message}`);
});
```

