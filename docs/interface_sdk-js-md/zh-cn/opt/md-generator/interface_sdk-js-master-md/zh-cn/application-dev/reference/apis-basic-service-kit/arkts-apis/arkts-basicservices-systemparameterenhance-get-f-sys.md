# get（系统接口）

## get

```TypeScript
function get(key: string, callback: AsyncCallback<string>): void
```

获取系统参数key对应的值，使用callback异步回调。

**起始版本：** 9

<!--Device-systemParameterEnhance-function get(key: string, callback: AsyncCallback<string>): void--><!--Device-systemParameterEnhance-function get(key: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-system-parameterV9.md#14700101-系统参数查找失败) |
| [14700103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemParameterEnhance.get('const.ohos.apiversion', (err: BusinessError, data: string) => {
    if (err) {
      console.error(`Failed to get const.ohos.apiversion value. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`get const.ohos.apiversion value success: ${data}`);
    }
  });
} catch (e) {
  console.error('get unexpected error: ' + e);
}
```


## get

```TypeScript
function get(key: string, def: string, callback: AsyncCallback<string>): void
```

获取系统参数Key对应的值，使用callback异步回调。

**起始版本：** 9

<!--Device-systemParameterEnhance-function get(key: string, def: string, callback: AsyncCallback<string>): void--><!--Device-systemParameterEnhance-function get(key: string, def: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| def | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-system-parameterV9.md#14700101-系统参数查找失败) |
| [14700103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemParameterEnhance.get('const.ohos.apiversion', 'default', (err: BusinessError, data: string) => {
    if (err) {
      console.error(`Failed to get const.ohos.apiversion value. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`get const.ohos.apiversion value success: ${data}`);
    }
  });
} catch (e) {
  console.error('get unexpected error: ' + e);
}
```


## get

```TypeScript
function get(key: string, def?: string): Promise<string>
```

获取系统参数key对应的值，使用Promise异步回调。

**起始版本：** 9

<!--Device-systemParameterEnhance-function get(key: string, def?: string): Promise<string>--><!--Device-systemParameterEnhance-function get(key: string, def?: string): Promise<string>-End-->

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| def | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14700101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-system-parameterV9.md#14700101-系统参数查找失败) |
| [14700103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise: Promise<string> = systemParameterEnhance.get('const.ohos.apiversion');
  promise.then((value: string) => {
    console.info('get const.ohos.apiversion success: ' + value);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get const.ohos.apiversion. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  console.error('get unexpected error: ' + e);
}
```
