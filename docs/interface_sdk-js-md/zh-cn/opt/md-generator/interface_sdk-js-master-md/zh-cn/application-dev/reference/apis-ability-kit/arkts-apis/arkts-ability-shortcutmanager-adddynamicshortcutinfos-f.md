# addDynamicShortcutInfos

## addDynamicShortcutInfos

```TypeScript
function addDynamicShortcutInfos(shortcutInfo: Array<ShortcutInfo>, userId: number): Promise<void>
```

添加指定用户的动态快捷方式。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_SHORTCUTS or (ohos.permission.MANAGE_SHORTCUTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

<!--Device-shortcutManager-function addDynamicShortcutInfos(shortcutInfo: Array<ShortcutInfo>, userId: int): Promise<void>--><!--Device-shortcutManager-function addDynamicShortcutInfos(shortcutInfo: Array<ShortcutInfo>, userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shortcutInfo | Array & lt;ShortcutInfo & gt; | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17700061](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700026-指定应用被禁用) |
| [18100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#18100001-shortcutinfo列表中bundlename和appindex不一一对应) |
| [17700070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700070-指定的快捷方式id不合法) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 请开发者替换为实际的快捷方式id、bundleName、moduleName、userId。
const bundleName = "com.example.dynamic";
let moduleName = 'entry';
const arrShortcutInfo: Array<shortcutManager.ShortcutInfo> = [
  {
    id: "1",
    bundleName: bundleName,
    moduleName: moduleName,
    appIndex: 0,
    sourceType: 2
  },
  {
    id: "2",
    bundleName: bundleName,
    moduleName: moduleName,
    appIndex: 0,
    sourceType: 2
  }
]

try {
  shortcutManager.addDynamicShortcutInfos(arrShortcutInfo, 100)
    .then(() => {
      console.info('addDynamicShortcutInfos success');
    }).catch((err: Error) => {
    console.error(`addDynamicShortcutInfos errData is errCode:${(err as BusinessError).code}  message:${(err as BusinessError).message}`);
  });
} catch (err) {
  console.error(`addDynamicShortcutInfos errData is errCode:${(err as BusinessError).code}  message:${(err as BusinessError).message}`);
}
```
