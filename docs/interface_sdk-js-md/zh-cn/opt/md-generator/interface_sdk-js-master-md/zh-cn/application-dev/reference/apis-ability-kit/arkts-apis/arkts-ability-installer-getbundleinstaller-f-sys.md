# getBundleInstaller（系统接口）

## getBundleInstaller

```TypeScript
function getBundleInstaller(callback: AsyncCallback<BundleInstaller>): void
```

获取BundleInstaller对象。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-installer-function getBundleInstaller(callback: AsyncCallback<BundleInstaller>): void--><!--Device-installer-function getBundleInstaller(callback: AsyncCallback<BundleInstaller>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;BundleInstaller&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## getBundleInstaller

```TypeScript
function getBundleInstaller(): Promise<BundleInstaller>
```

获取BundleInstaller对象。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-installer-function getBundleInstaller(): Promise<BundleInstaller>--><!--Device-installer-function getBundleInstaller(): Promise<BundleInstaller>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;BundleInstaller & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
