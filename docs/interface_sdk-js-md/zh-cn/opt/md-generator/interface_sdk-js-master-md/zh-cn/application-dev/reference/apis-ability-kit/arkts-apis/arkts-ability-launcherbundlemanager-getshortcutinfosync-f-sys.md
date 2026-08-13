# getShortcutInfoSync（系统接口）

## getShortcutInfoSync

```TypeScript
function getShortcutInfoSync(bundleName: string): Array<ShortcutInfo>
```

查询当前用户下指定应用的快捷方式信息ShortcutInfo，只支持查询主应用的ShortcutInfo，查询分身应用请使用 [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getShortcutInfoByAppIndex（系统接口）)。 获取调用方自身的信息时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-launcherBundleManager-function getShortcutInfoSync(bundleName: string): Array<ShortcutInfo>--><!--Device-launcherBundleManager-function getShortcutInfoSync(bundleName: string): Array<ShortcutInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;ShortcutInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = launcherBundleManager.getShortcutInfoSync("com.example.demo");
  console.info('data is ' + JSON.stringify(data));
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```


## getShortcutInfoSync

```TypeScript
function getShortcutInfoSync(bundleName: string, userId: number): Array<ShortcutInfo>
```

查询指定用户下指定应用的快捷方式信息ShortcutInfo，只支持查询主应用的ShortcutInfo，查询分身应用请使用 [getShortcutInfoByAppIndex](arkts-ability-launcherbundlemanager-getshortcutinfobyappindex-f-sys.md#getShortcutInfoByAppIndex（系统接口）)。 获取调用方自身的信息时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-launcherBundleManager-function getShortcutInfoSync(bundleName: string, userId: int): Array<ShortcutInfo>--><!--Device-launcherBundleManager-function getShortcutInfoSync(bundleName: string, userId: int): Array<ShortcutInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;ShortcutInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = launcherBundleManager.getShortcutInfoSync("com.example.demo", 100);
  console.info('data is ' + JSON.stringify(data));
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```
