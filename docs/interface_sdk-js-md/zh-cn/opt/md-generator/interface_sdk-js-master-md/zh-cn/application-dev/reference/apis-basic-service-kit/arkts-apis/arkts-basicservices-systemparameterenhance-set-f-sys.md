# set（系统接口）

## set

```TypeScript
function set(key: string, value: string, callback: AsyncCallback<void>): void
```

设置系统参数key对应的值，使用callback异步回调。

**起始版本：** 9

<!--Device-systemParameterEnhance-function set(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-systemParameterEnhance-function set(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14700102](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../../apis-basic-services-kit/errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemParameterEnhance.set('test.parameter.key', 'testValue', (err: BusinessError, data: void) => {
    if (err) {
      console.error(`Failed to set test.parameter.key value. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('set test.parameter.key value success');
    }
  });
} catch (e) {
  console.error('set unexpected error: ' + e);
}
```


## set

```TypeScript
function set(key: string, value: string): Promise<void>
```

设置系统参数key对应的值，使用Promise异步回调。

**起始版本：** 9

<!--Device-systemParameterEnhance-function set(key: string, value: string): Promise<void>--><!--Device-systemParameterEnhance-function set(key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Startup.SystemInfo

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14700102](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../../apis-basic-services-kit/errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise: Promise<void> = systemParameterEnhance.set('test.parameter.key', 'testValue');
  promise.then((value: void) => {
    console.info('set test.parameter.key success: ' + value);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set test.parameter.key. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  console.error('set unexpected error: ' + e);
}
```
