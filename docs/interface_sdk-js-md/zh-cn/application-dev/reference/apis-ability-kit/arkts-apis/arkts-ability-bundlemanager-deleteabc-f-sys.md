# deleteAbc（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## deleteAbc

```TypeScript
function deleteAbc(abcPath: string): Promise<void>
```

根据给定的abcPath删除.abc文件。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.RUN_DYN_CODE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| abcPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700202](../errorcode-bundle.md#17700202-abc文件删除失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
