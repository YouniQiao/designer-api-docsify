# generateDLPFile（系统接口）

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## generateDLPFile

```TypeScript
function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty): Promise<DLPFile>
```

DLP管理应用调用该接口，将明文文件加密生成DLPFile管理对象，对象仅在授权列表内的用户可以打开，授权又分为完全控制权限和只读权限。使用Promise异步回调。调用generateDLPFile成功后返回DLPFile对象，必须在使用完毕后调用closeDLPFile释放资源。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plaintextFd | number | 是 |
| ciphertextFd | number | 是 |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |
| [19100005](../errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100009](../errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |


## generateDLPFile

```TypeScript
function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty, callback: AsyncCallback<DLPFile>): void
```

DLP管理应用调用该接口，将明文文件加密生成权限受控文件，仅在授权列表内的用户可以打开，授权又分为完全控制权限和只读权限。获取DLPFile管理对象，使用callback异步回调。使用完DLPFile对象后，应调用 closeDLPFile释放对象，避免资源泄露。调用generateDLPFile()成功后返回DLPFile对象，必须在使用完毕后调用closeDLPFile()释放资源。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plaintextFd | number | 是 |
| ciphertextFd | number | 是 |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |
| [19100005](../errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100009](../errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
