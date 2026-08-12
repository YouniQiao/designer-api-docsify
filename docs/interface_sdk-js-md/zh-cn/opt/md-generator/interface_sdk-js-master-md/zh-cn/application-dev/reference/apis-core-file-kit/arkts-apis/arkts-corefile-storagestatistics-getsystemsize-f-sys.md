# getSystemSize（系统接口）

## getSystemSize

```TypeScript
function getSystemSize(callback: AsyncCallback<number>): void
```

异步获取系统数据的空间大小（单位为Byte），以callback方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getSystemSize(callback: AsyncCallback<long>): void--><!--Device-storageStatistics-function getSystemSize(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getSystemSize((error: BusinessError, number: number) => {
  if (error) {
    console.error(`getSystemSize failed with err, code is: ${error.code}, message is: ${error.message}`);
  } else {
    // do something
    console.info("getSystemSize successfully:" + number);
  }
});
```


## getSystemSize

```TypeScript
function getSystemSize(): Promise<number>
```

异步获取系统数据的空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getSystemSize(): Promise<long>--><!--Device-storageStatistics-function getSystemSize(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getSystemSize().then((number: number) => {
  console.info("getSystemSize successfully:" + number);
}).catch((err: BusinessError) => {
  console.error(`getSystemSize failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
