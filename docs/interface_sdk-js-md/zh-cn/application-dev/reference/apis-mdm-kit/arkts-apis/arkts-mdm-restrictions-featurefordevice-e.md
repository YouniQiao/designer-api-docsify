# FeatureForDevice

设备特性枚举。

**起始版本：** 24

<!--Device-restrictions-enum FeatureForDevice--><!--Device-restrictions-enum FeatureForDevice-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## WIFI_P2P

```TypeScript
WIFI_P2P = 0
```

Wi-Fi P2P（点对点连接），允许设备在没有接入点的情况下直接相互连接。禁用后，设备无法通过Wi-Fi P2P进行点对点连接，影响文件传输、游戏联机、屏幕共享等需要直接Wi-Fi连接的应用功能。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-WIFI_P2P = 0--><!--Device-FeatureForDevice-WIFI_P2P = 0-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## LOCAL_INPUT

```TypeScript
LOCAL_INPUT = 2
```

本地输入（包含键盘、鼠标、触控板、触摸屏等）被禁用后，无法通过本地输入进行操作。重启设备可解除禁用。在息屏状态下禁用会导致屏幕无法唤醒，若禁用后屏幕自动息屏，同样会导致无法唤醒屏幕。

26.0.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-LOCAL_INPUT = 2--><!--Device-FeatureForDevice-LOCAL_INPUT = 2-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## SUDO

```TypeScript
SUDO = 4
```

超级用户执行

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-SUDO = 4--><!--Device-FeatureForDevice-SUDO = 4-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## TRAFFIC_REDIRECTION

```TypeScript
TRAFFIC_REDIRECTION = 5
```

流量重定向

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-TRAFFIC_REDIRECTION = 5--><!--Device-FeatureForDevice-TRAFFIC_REDIRECTION = 5-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## CORE_DUMP

```TypeScript
CORE_DUMP = 6
```

创建文件转储。禁用后，无法通过任务管理器创建文件转储。

26.0.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-CORE_DUMP = 6--><!--Device-FeatureForDevice-CORE_DUMP = 6-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## RS232

```TypeScript
RS232 = 7
```

RS232串口

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-RS232 = 7--><!--Device-FeatureForDevice-RS232 = 7-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## DISK_ERASURE

```TypeScript
DISK_ERASURE = 8
```

安全擦除

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-DISK_ERASURE = 8--><!--Device-FeatureForDevice-DISK_ERASURE = 8-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## BLUETOOTH

```TypeScript
BLUETOOTH = 9
```

设备蓝牙能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-BLUETOOTH = 9--><!--Device-FeatureForDevice-BLUETOOTH = 9-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MODIFY_DATE_TIME

```TypeScript
MODIFY_DATE_TIME = 10
```

安全擦除

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MODIFY_DATE_TIME = 10--><!--Device-FeatureForDevice-MODIFY_DATE_TIME = 10-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## PRINTER

```TypeScript
PRINTER = 11
```

设备打印能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-PRINTER = 11--><!--Device-FeatureForDevice-PRINTER = 11-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## HDC

```TypeScript
HDC = 12
```

被其他设备通过hdc连接、调试的能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-HDC = 12--><!--Device-FeatureForDevice-HDC = 12-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MICROPHONE

```TypeScript
MICROPHONE = 13
```

设备麦克风能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MICROPHONE = 13--><!--Device-FeatureForDevice-MICROPHONE = 13-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## FINGERPRINT

```TypeScript
FINGERPRINT = 14
```

设备指纹认证能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-FINGERPRINT = 14--><!--Device-FeatureForDevice-FINGERPRINT = 14-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## USB

```TypeScript
USB = 15
```

设备USB能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-USB = 15--><!--Device-FeatureForDevice-USB = 15-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## WIFI

```TypeScript
WIFI = 16
```

设备Wi-Fi能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-WIFI = 16--><!--Device-FeatureForDevice-WIFI = 16-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## TETHERING

```TypeScript
TETHERING = 17
```

网络共享能力（设备已有网络共享给其他设备的能力，即共享热点能力）。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-TETHERING = 17--><!--Device-FeatureForDevice-TETHERING = 17-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## INACTIVE_USER_FREEZE

```TypeScript
INACTIVE_USER_FREEZE = 18
```

非活跃用户运行能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-INACTIVE_USER_FREEZE = 18--><!--Device-FeatureForDevice-INACTIVE_USER_FREEZE = 18-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## CAMERA

```TypeScript
CAMERA = 19
```

设备相机能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-CAMERA = 19--><!--Device-FeatureForDevice-CAMERA = 19-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MTP_CLIENT

```TypeScript
MTP_CLIENT = 20
```

MTP客户端能力（包含读取和写入）

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MTP_CLIENT = 20--><!--Device-FeatureForDevice-MTP_CLIENT = 20-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MTP_SERVER

```TypeScript
MTP_SERVER = 21
```

MTP服务端能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MTP_SERVER = 21--><!--Device-FeatureForDevice-MTP_SERVER = 21-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## SAMBA_CLIENT

```TypeScript
SAMBA_CLIENT = 22
```

samba客户端能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-SAMBA_CLIENT = 22--><!--Device-FeatureForDevice-SAMBA_CLIENT = 22-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## SAMBA_SERVER

```TypeScript
SAMBA_SERVER = 23
```

samba服务端能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-SAMBA_SERVER = 23--><!--Device-FeatureForDevice-SAMBA_SERVER = 23-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## BACKUP_AND_RESTORE

```TypeScript
BACKUP_AND_RESTORE = 24
```

备份和恢复能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-BACKUP_AND_RESTORE = 24--><!--Device-FeatureForDevice-BACKUP_AND_RESTORE = 24-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MAINTENANCE_MODE

```TypeScript
MAINTENANCE_MODE = 25
```

设备维修模式能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MAINTENANCE_MODE = 25--><!--Device-FeatureForDevice-MAINTENANCE_MODE = 25-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MMS

```TypeScript
MMS = 26
```

设备接收、发送彩信的能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MMS = 26--><!--Device-FeatureForDevice-MMS = 26-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## SMS

```TypeScript
SMS = 27
```

设备接收、发送短信的能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-SMS = 27--><!--Device-FeatureForDevice-SMS = 27-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## MOBILE_DATA

```TypeScript
MOBILE_DATA = 28
```

蜂窝数据能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-MOBILE_DATA = 28--><!--Device-FeatureForDevice-MOBILE_DATA = 28-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## AIRPLANE_MODE

```TypeScript
AIRPLANE_MODE = 29
```

飞行模式能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-AIRPLANE_MODE = 29--><!--Device-FeatureForDevice-AIRPLANE_MODE = 29-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## VPN

```TypeScript
VPN = 30
```

Virtual Private Network（虚拟专用网络），VPN能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-VPN = 30--><!--Device-FeatureForDevice-VPN = 30-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## NOTIFICATION

```TypeScript
NOTIFICATION = 31
```

设备通知能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-NOTIFICATION = 31--><!--Device-FeatureForDevice-NOTIFICATION = 31-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## NFC

```TypeScript
NFC = 32
```

Near Field Communication（近距离无线通信），NFC能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-NFC = 32--><!--Device-FeatureForDevice-NFC = 32-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## PRIVATE_SPACE

```TypeScript
PRIVATE_SPACE = 33
```

创建隐私空间能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-PRIVATE_SPACE = 33--><!--Device-FeatureForDevice-PRIVATE_SPACE = 33-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## TELEPHONE_CALL

```TypeScript
TELEPHONE_CALL = 34
```

设备通话能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-TELEPHONE_CALL = 34--><!--Device-FeatureForDevice-TELEPHONE_CALL = 34-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## APP_CLONE

```TypeScript
APP_CLONE = 35
```

应用分身能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-APP_CLONE = 35--><!--Device-FeatureForDevice-APP_CLONE = 35-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## EXTERNAL_STORAGE_CARD

```TypeScript
EXTERNAL_STORAGE_CARD = 36
```

外置存储能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-EXTERNAL_STORAGE_CARD = 36--><!--Device-FeatureForDevice-EXTERNAL_STORAGE_CARD = 36-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## RANDOM_MAC

```TypeScript
RANDOM_MAC = 37
```

Wi-Fi连接时使用随机MAC能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-RANDOM_MAC = 37--><!--Device-FeatureForDevice-RANDOM_MAC = 37-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## UNMUTE_DEVICE

```TypeScript
UNMUTE_DEVICE = 38
```

设备媒体播放声音能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-UNMUTE_DEVICE = 38--><!--Device-FeatureForDevice-UNMUTE_DEVICE = 38-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## HDC_REMOTE

```TypeScript
HDC_REMOTE = 39
```

设备通过hdc调试其他设备的能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-HDC_REMOTE = 39--><!--Device-FeatureForDevice-HDC_REMOTE = 39-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## VIRTUAL_SERVICE

```TypeScript
VIRTUAL_SERVICE = 40
```

设备虚拟化服务能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-VIRTUAL_SERVICE = 40--><!--Device-FeatureForDevice-VIRTUAL_SERVICE = 40-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## USB_SERIAL

```TypeScript
USB_SERIAL = 41
```

设备USB转串口能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-USB_SERIAL = 41--><!--Device-FeatureForDevice-USB_SERIAL = 41-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## SCREEN_SHOT

```TypeScript
SCREEN_SHOT = 42
```

设备截屏能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-SCREEN_SHOT = 42--><!--Device-FeatureForDevice-SCREEN_SHOT = 42-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## SCREEN_RECORD

```TypeScript
SCREEN_RECORD = 43
```

设备录屏能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-SCREEN_RECORD = 43--><!--Device-FeatureForDevice-SCREEN_RECORD = 43-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## DISK_RECOVERY_KEY

```TypeScript
DISK_RECOVERY_KEY = 44
```

恢复密钥导出能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-DISK_RECOVERY_KEY = 44--><!--Device-FeatureForDevice-DISK_RECOVERY_KEY = 44-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## NEAR_LINK

```TypeScript
NEAR_LINK = 45
```

设备星闪能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-NEAR_LINK = 45--><!--Device-FeatureForDevice-NEAR_LINK = 45-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## DEVELOPER_MODE

```TypeScript
DEVELOPER_MODE = 46
```

开发者模式

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-DEVELOPER_MODE = 46--><!--Device-FeatureForDevice-DEVELOPER_MODE = 46-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## RESET_FACTORY

```TypeScript
RESET_FACTORY = 47
```

恢复出厂能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-RESET_FACTORY = 47--><!--Device-FeatureForDevice-RESET_FACTORY = 47-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## REMOTE_DESK

```TypeScript
REMOTE_DESK = 48
```

远程桌面能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-REMOTE_DESK = 48--><!--Device-FeatureForDevice-REMOTE_DESK = 48-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## REMOTE_DIAGNOSIS

```TypeScript
REMOTE_DIAGNOSIS = 49
```

远程诊断能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-REMOTE_DIAGNOSIS = 49--><!--Device-FeatureForDevice-REMOTE_DIAGNOSIS = 49-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## OTA_UPDATE

```TypeScript
OTA_UPDATE = 50
```

公网环境下系统升级能力

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FeatureForDevice-OTA_UPDATE = 50--><!--Device-FeatureForDevice-OTA_UPDATE = 50-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

