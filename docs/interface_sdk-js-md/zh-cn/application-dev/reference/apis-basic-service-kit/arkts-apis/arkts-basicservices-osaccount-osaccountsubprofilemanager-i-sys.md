# OsAccountSubProfileManager（系统接口）

系统账号子身份资料管理器类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-osAccount-interface OsAccountSubProfileManager--><!--Device-osAccount-interface OsAccountSubProfileManager-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;OsAccountSubProfile&gt; | Promise对象，返回创建的子身份资料。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12300010 | Service busy. Possible causes: The target OS account is being operated. |
| 12300008 | Restricted OS account. |
| 12300003 | The OS account not found. |
| 201 | Permission denied. |
| 12300402 | The number of sub-profiles under the OS account has reached limit. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## 示例

创建ID为100的系统账号的子身份资料。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 子身份资料的标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12300010 | Service busy. Possible causes: The OS account or sub-profile is being operated. |
| 12300403 | Restricted sub-profile cannot be deleted. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |
| 12300404 | The foreground sub-profile cannot be deleted. |

## 示例

删除ID为100的系统账号中ID为100001的子身份资料。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回系统账号的前台子身份资料标识符。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## 示例

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回系统账号前台子身份资料的标识符。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12300003 | OS account not found. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | The foreground sub-profile not found. |

## 示例

获取ID为100的系统账号的前台子身份资料标识符。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 子身份资料的标识符 &lt;br&gt;取值范围为全体整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回子身份资料所属系统账号的本地ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## 示例

获取ID为100001的子身份资料所属的系统账号本地标识符。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 子身份资料的标识符 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;OsAccountSubProfile&gt; | Promise对象，返回子身份资料对象信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## 示例

获取ID为100001的子身份资料对象信息。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 子身份资料的标识符。 &lt;br&gt;取值范围为全体整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;OsAccountSubProfile&gt; | Promise对象，返回子身份资料对象信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |

## 示例

获取ID为100的系统账号中ID为100001的子身份资料对象信息。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Promise used to return the ID list of sub-profile. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## 示例

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Promise used to return the ID list of sub-profile. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12300003 | OS account not found. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## 示例

获取ID为100的系统账号的子身份资料标识符列表。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void--><!--Device-OsAccountSubProfileManager-offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;OsAccountSubProfileEventData&gt; | 否 | 需要取消订阅的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Not system application. |
| 12300001 | System service exception. |

## 示例

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-onOsAccountSubProfileEvent(      events: OsAccountSubProfileEvent[],      callback: Callback<OsAccountSubProfileEventData>): void--><!--Device-OsAccountSubProfileManager-onOsAccountSubProfileEvent(      events: OsAccountSubProfileEvent[],      callback: Callback<OsAccountSubProfileEventData>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| events | [OsAccountSubProfileEvent](arkts-basicservices-osaccount-osaccountsubprofileevent-e-sys.md)[] | 是 | 要订阅的事件数组 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;OsAccountSubProfileEventData&gt; | 是 | 事件发生时调用的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12300002 | Invalid event. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## 示例

订阅系统账号子身份的创建事件。

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

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| osAccountLocalId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 系统账号的本地标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |
| subProfileId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 子身份资料的标识符。 &lt;br&gt;取值范围为全体整数。 &lt;br&gt;The value range is all integers. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12300010 | Service busy. Possible causes: The OS account or sub-profile is being operated. |
| 12300403 | Restricted sub-profile cannot be switched to foreground. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 12300001 | System service exception. |
| 12300401 | Sub-profile not found. |
| 12300405 | The foreground sub-profile bound with a logged-in distributed account cannot be directly switched to background. |

## 示例

将ID为100的系统账号的当前子身份资料切换到ID为100001的子身份资料。

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

