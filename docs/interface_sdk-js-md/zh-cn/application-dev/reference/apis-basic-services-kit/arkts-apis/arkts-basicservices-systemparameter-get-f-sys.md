# get（系统接口）

## 导入模块

```TypeScript
import { systemParameter } from '@kit.BasicServicesKit';
```

## get

```TypeScript
function get(key: string, callback: AsyncCallback<string>): void
```

获取系统参数key对应的值，使用callback异步回调。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** get

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14700102](../errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';

try {
  systemParameter.get('const.ohos.apiversion', (err: BusinessError, data: string) => {
    if (err) {
      console.error(`Failed to get system parameter. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('get const.ohos.apiversion success: ' + data);
    }
  });
} catch (e) {
  console.error('get unexpected error: ' + e);
}
```

```TypeScript
import { BusinessError } from '@ohos.base';

try {
  systemParameter.get('const.ohos.apiversion', 'default', (err: BusinessError, data: string) => {
    if (err) {
      console.error(`Failed to get system parameter. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('get const.ohos.apiversion success: ' + data);
    }
  });
} catch (e) {
  console.error('get unexpected error: ' + e);
}
```

```TypeScript
import { BusinessError } from '@ohos.base';

try {
  let getPromise: Promise<string> = systemParameter.get('const.ohos.apiversion');
  getPromise.then((value: string) => {
    console.info('get const.ohos.apiversion success: ' + value);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get system parameter. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  console.error('get unexpected error: ' + e);
}
```


## get

```TypeScript
function get(key: string, def: string, callback: AsyncCallback<string>): void
```

获取系统参数key对应的值，使用callback异步回调。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** get

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14700102](../errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

**示例**

参见 [get](#get)


## get

```TypeScript
function get(key: string, def?: string): Promise<string>
```

获取系统参数key对应的值，使用Promise异步回调。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** get

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14700102](../errorcode-system-parameterV9.md#14700102-系统参数值无效) |
| [14700103](../errorcode-device-info.md#14700103-操作因权限被拒绝) |
| [14700104](../errorcode-system-parameterV9.md#14700104-系统内部错误包括内存不足死锁等) |

**示例**

参见 [get](#get)
