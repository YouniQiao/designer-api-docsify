# OsAccountSubProfileManager (System API)

系统账号子身份资料管理器类。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-osAccount-interface OsAccountSubProfileManager--><!--Device-osAccount-interface OsAccountSubProfileManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## createOsAccountSubProfile

ArkTS-Dyn:
```TypeScript
createOsAccountSubProfile(osAccountLocalId: number): Promise<OsAccountSubProfile>
```

ArkTS-Sta:
```TypeScript
createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>
```

创建一个系统账号子身份资料。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OsAccountSubProfile&gt; | Promise对象，返回创建的子身份资料。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300010 | Service busy. Possible causes: The target OS account is being operated. |
| 12300008 | Restricted OS account. |
| 12300003 | The OS account not found. |
| 201 | Permission denied. |
| 12300402 | The number of sub-profiles under the OS account has reached limit. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## Examples

Create an OS account sub-profile whose ID is 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
try {
  subProfileManager.createOsAccountSubProfile(osAccountLocalId).then((subProfile: osAccount.OsAccountSubProfile) => {
    console.info('createOsAccountSubProfile successfully, subProfileId: ' + subProfile.id);
  }).catch((err: BusinessError) => {
    console.error(`createOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## deleteOsAccountSubProfile

ArkTS-Dyn:
```TypeScript
deleteOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>
```

删除一个系统账号子身份资料。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 子身份资料的标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300010 | Service busy. Possible causes: The OS account or sub-profile is being operated. |
| 12300403 | Restricted sub-profile cannot be deleted. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |
| 12300404 | The foreground sub-profile cannot be deleted. |

## Examples

Delete the sub-profile whose ID is 100001 from OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
let subProfileId: number = 100001;
try {
  subProfileManager.deleteOsAccountSubProfile(osAccountLocalId, subProfileId).then(() => {
    console.info('deleteOsAccountSubProfile successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountForegroundSubProfileId

ArkTS-Dyn:
```TypeScript
getOsAccountForegroundSubProfileId(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getOsAccountForegroundSubProfileId(): Promise<int>
```

获取调用方所属系统账号的前台子身份资料的标识符。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回系统账号的前台子身份资料标识符。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
try {
  subProfileManager.getOsAccountForegroundSubProfileId().then((subProfileId: number) => {
    console.info('getOsAccountForegroundSubProfileId successfully, subProfileId: ' + subProfileId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountForegroundSubProfileId failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountForegroundSubProfileId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountForegroundSubProfileId

ArkTS-Dyn:
```TypeScript
getOsAccountForegroundSubProfileId(osAccountLocalId: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>
```

获取指定系统账号的前台子身份资料标识符。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回系统账号前台子身份资料的标识符。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300003 | OS account not found. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | The foreground sub-profile not found. |

## Examples

Obtain the foreground sub-profile ID of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
try {
  subProfileManager.getOsAccountForegroundSubProfileId(osAccountLocalId).then((subProfileId: number) => {
    console.info('getOsAccountForegroundSubProfileId successfully, subProfileId: ' + subProfileId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountForegroundSubProfileId failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountForegroundSubProfileId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountLocalIdForSubProfile

ArkTS-Dyn:
```TypeScript
getOsAccountLocalIdForSubProfile(subProfileId: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>
```

获取子身份资料所属系统账号的本地标识符。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 子身份资料的标识符 &lt;br&gt;取值范围为全体整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回子身份资料所属系统账号的本地ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## Examples

Obtains the local ID of the OS account of the sub-profile whose ID is 100001.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let subProfileId: number = 100001;
try {
  subProfileManager.getOsAccountLocalIdForSubProfile(subProfileId).then((osAccountLocalId: number) => {
    console.info('getOsAccountLocalIdForSubProfile successfully, osAccountLocalId: ' + osAccountLocalId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIdForSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfile

ArkTS-Dyn:
```TypeScript
getOsAccountSubProfile(subProfileId: number): Promise<OsAccountSubProfile>
```

ArkTS-Sta:
```TypeScript
getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>
```

获取调用方所属系统账号的子身份资料对象信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 子身份资料的标识符 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OsAccountSubProfile&gt; | Promise对象，返回子身份资料对象信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## Examples

Obtains the sub-profile whose ID is 100001.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let subProfileId: number = 100001;
try {
  subProfileManager.getOsAccountSubProfile(subProfileId).then((subProfile: osAccount.OsAccountSubProfile) => {
    console.info('getOsAccountSubProfile successfully, subProfile: ' + JSON.stringify(subProfile));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfile

ArkTS-Dyn:
```TypeScript
getOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<OsAccountSubProfile>
```

ArkTS-Sta:
```TypeScript
getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>
```

获取指定系统账号的子身份资料对象信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 子身份资料的标识符。 &lt;br&gt;取值范围为全体整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;OsAccountSubProfile&gt; | Promise对象，返回子身份资料对象信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## Examples

Obtain the sub-profile whose ID is 100001 of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
let subProfileId: number = 100001;
try {
  subProfileManager.getOsAccountSubProfile(osAccountLocalId, subProfileId).then((subProfile: osAccount.OsAccountSubProfile) => {
    console.info('getOsAccountSubProfile successfully, subProfile: ' + JSON.stringify(subProfile));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfileIds

ArkTS-Dyn:
```TypeScript
getOsAccountSubProfileIds(): Promise<number[]>
```

ArkTS-Sta:
```TypeScript
getOsAccountSubProfileIds(): Promise<int[]>
```

获取调用者所属系统账号的子身份资料标识符列表。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Promise used to return the ID list of sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
try {
  subProfileManager.getOsAccountSubProfileIds().then((subProfileIds: number[]) => {
    console.info('getOsAccountSubProfileIds successfully, subProfileIds: ' + subProfileIds);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfileIds failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfileIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfileIds

ArkTS-Dyn:
```TypeScript
getOsAccountSubProfileIds(osAccountLocalId: number): Promise<number[]>
```

ArkTS-Sta:
```TypeScript
getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>
```

获取指定系统账号的子身份资料标识符列表。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Promise used to return the ID list of sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300003 | OS account not found. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## Examples

Obtain the sub-profile IDs of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
try {
  subProfileManager.getOsAccountSubProfileIds(osAccountLocalId).then((subProfileIds: number[]) => {
    console.info('getOsAccountSubProfileIds successfully, subProfileIds: ' + subProfileIds);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfileIds failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfileIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## offOsAccountSubProfileEvent

```TypeScript
offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void
```

取消订阅系统账号子身份资料的事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void--><!--Device-OsAccountSubProfileManager-offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;OsAccountSubProfileEventData&gt; | No | 需要取消订阅的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |
| 12300001 | System service exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
try {
  subProfileManager.offOsAccountSubProfileEvent();
} catch (e) {
  const err = e as BusinessError;
  console.error(`offOsAccountSubProfileEvent failed, code is ${err.code}, message is ${err.message}`);
}
```

## onOsAccountSubProfileEvent

```TypeScript
onOsAccountSubProfileEvent(
      events: OsAccountSubProfileEvent[],
      callback: Callback<OsAccountSubProfileEventData>): void
```

订阅系统账号子身份资料的事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-onOsAccountSubProfileEvent(      events: OsAccountSubProfileEvent[],      callback: Callback<OsAccountSubProfileEventData>): void--><!--Device-OsAccountSubProfileManager-onOsAccountSubProfileEvent(      events: OsAccountSubProfileEvent[],      callback: Callback<OsAccountSubProfileEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| events | [OsAccountSubProfileEvent](arkts-basicservices-osaccount-osaccountsubprofileevent-e-sys.md)[] | Yes | 要订阅的事件数组 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;OsAccountSubProfileEventData&gt; | Yes | 事件发生时调用的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300002 | Invalid event. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## Examples

Subscribe to an OS account sub-profile creation event.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let events: osAccount.OsAccountSubProfileEvent[] = [osAccount.OsAccountSubProfileEvent.CREATED];
try {
  subProfileManager.onOsAccountSubProfileEvent(events, (data: osAccount.OsAccountSubProfileEventData) => {
    console.info('onOsAccountSubProfileEvent, event: ' + data.event + ', localId: ' + data.osAccountLocalId);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`onOsAccountSubProfileEvent failed, code is ${err.code}, message is ${err.message}`);
}
```

## switchOsAccountSubProfile

ArkTS-Dyn:
```TypeScript
switchOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>
```

切换至一个系统账号子身份资料。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 子身份资料的标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300010 | Service busy. Possible causes: The OS account or sub-profile is being operated. |
| 12300403 | Restricted sub-profile cannot be switched to foreground. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |
| 12300405 | The foreground sub-profile bound with a logged-in distributed account cannot be directly switched to background. |

## Examples

Switch from the current sub-profile of OS account 100 to the sub-profile whose ID is 100001.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
let subProfileId: number = 100001;
try {
  subProfileManager.switchOsAccountSubProfile(osAccountLocalId, subProfileId).then(() => {
    console.info('switchOsAccountSubProfile successfully');
  }).catch((err: BusinessError) => {
    console.error(`switchOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`switchOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

