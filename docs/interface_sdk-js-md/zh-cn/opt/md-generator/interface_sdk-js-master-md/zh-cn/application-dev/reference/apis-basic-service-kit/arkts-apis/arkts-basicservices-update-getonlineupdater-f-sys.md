# getOnlineUpdater（系统接口）

## 导入模块

```TypeScript
```

## getOnlineUpdater

```TypeScript
function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater
```

获取在线升级对象，可用于在线检查新版本、下载升级包、安装升级包等操作。适用于设备厂商的OTA(详见[术语](../../../basic-services/update/update-kit-term.md))升级客户端应用、在 线系统升级等场景，帮助用户及时获取系统更新，提升升级效率和用户体验。 **原理说明**： 该方法通过系统服务接口获取在线升级对象，该对象提供检查新版本、下载升级包、安装升级包等核心功能。 **约束和限制**： - 检查新版本和下载升级包都必须依赖设备厂商部署的升级包管理服务器。

**起始版本：** 23

<!--Device-update-function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater--><!--Device-update-function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater-End-->

**系统能力：** SystemCapability.Update.UpdateService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| upgradeInfo | [UpgradeInfo](arkts-basicservices-update-upgradeinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Updater](arkts-basicservices-update-updater-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
// 定义升级信息对象
  const upgradeInfo: update.UpgradeInfo = {
    upgradeApp: 'com.ohos.ota.updateclient',  // 调用方包名
    businessType: {
      vendor: update.BusinessVendor.PUBLIC, // 供应商类型
      subType: update.BusinessSubType.FIRMWARE // 升级类型为固件
    }
  };  
  // 获取在线升级对象
  let onlineUpdater = update.getOnlineUpdater(upgradeInfo);
```
