# getAllShortcutInfoForSelf

## 导入模块

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## getAllShortcutInfoForSelf

```TypeScript
function getAllShortcutInfoForSelf(): Promise<Array<ShortcutInfo>>
```

查询当前应用[配置文件](../../../quick-start/module-configuration-file.md#shortcuts标签)中定义的所有快捷方式信息。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ShortcutInfo & gt; & gt; |
