# getSystemSize（系统接口）

## 导入模块

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getSystemSize

```TypeScript
function getSystemSize(callback: AsyncCallback<long>): void
```

异步获取系统数据的空间大小（单位为Byte），以callback方式返回。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getSystemSize().then((systemSize: number) => {
  console.info("getSystemSize successfully:" + systemSize);
}).catch((err: BusinessError) => {
  console.error(`getSystemSize failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getSystemSize().then((systemSize: long) => {
  console.info("getSystemSize successfully:" + systemSize);
}).catch((err: BusinessError): void => {
  console.error(`getSystemSize failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getSystemSize((error: BusinessError, systemSize: number) => {
  if (error) {
    console.error(`getSystemSize failed with err, code is: ${error.code}, message is: ${error.message}`);
  } else {
    // do something
    console.info("getSystemSize successfully:" + systemSize);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getSystemSize((error: BusinessError, systemSize: long): void => {
  if (error) {
    console.error(`getSystemSize failed with err, code is: ${error.code}, message is: ${error.message}`);
  } else {
    // do something
    console.info("getSystemSize successfully:" + systemSize);
  }
});
```


## getSystemSize

```TypeScript
function getSystemSize(): Promise<long>
```

异步获取系统数据的空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;long & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13900042 |

**示例**

参见 [getSystemSize](#getsystemsize)
