# isInSandbox

## isInSandbox

```TypeScript
function isInSandbox(): Promise<boolean>
```

查询当前应用是否运行在DLP沙箱环境。使用Promise异步回调。

该接口用于判断当前应用是否处于DLP沙箱环境，以便决定是否执行沙箱相关的操作或调用沙箱专用接口。

**起始版本：** 10

<!--Device-dlpPermission-function isInSandbox(): Promise<boolean>--><!--Device-dlpPermission-function isInSandbox(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isInSandbox().then((isInSandbox) => { // 是否在沙箱内。
  console.info('isInSandbox', isInSandbox);
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## isInSandbox

```TypeScript
function isInSandbox(callback: AsyncCallback<boolean>): void
```

查询当前应用是否运行在DLP沙箱环境。使用callback异步回调。

该接口用于判断当前应用是否处于DLP沙箱环境，以便决定是否执行沙箱相关的操作或调用沙箱专用接口。

**起始版本：** 10

<!--Device-dlpPermission-function isInSandbox(callback: AsyncCallback<boolean>): void--><!--Device-dlpPermission-function isInSandbox(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isInSandbox((err, isInSandbox) => {
  if (err) {
    console.error('isInSandbox error', err.code, err.message);
  } else {
    console.info('isInSandbox：', JSON.stringify(isInSandbox));
  }
}); // 是否在沙箱内。
```
