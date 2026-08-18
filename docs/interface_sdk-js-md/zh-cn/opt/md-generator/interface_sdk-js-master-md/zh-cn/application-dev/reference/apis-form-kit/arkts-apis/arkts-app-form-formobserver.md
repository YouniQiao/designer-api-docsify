# @ohos.app.form.formObserver

formObserver模块提供了卡片监听方相关接口的能力，包括对同一用户下安装的卡片新增、删除、可见性变化事件的订阅和取消订阅，获取正在运行的卡片信息等。 > **说明：** > > 本模块接口均为系统接口。

**起始版本：** 23

<!--Device-unnamed-declare namespace formObserver--><!--Device-unnamed-declare namespace formObserver-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid系统接口) |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid系统接口) |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid系统接口) |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid系统接口) |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos系统接口) |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos系统接口) |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos系统接口) |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos系统接口) |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getrunningforminfosbyfilter系统接口) |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getrunningforminfosbyfilter系统接口) |
| [offCall](arkts-form-formobserver-offcall-f-sys.md#offcall) |
| [offFormAdd](arkts-form-formobserver-offformadd-f-sys.md#offformadd) |
| [offFormRemove](arkts-form-formobserver-offformremove-f-sys.md#offformremove) |
| [offMessage](arkts-form-formobserver-offmessage-f-sys.md#offmessage) |
| [offNotifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md#offnotifyinvisible) |
| [offNotifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md#offnotifyvisible) |
| [offRouter](arkts-form-formobserver-offrouter-f-sys.md#offrouter) |
| [off_call](arkts-form-formobserver-offcall-f-sys.md#offcall) |
| [off_formAdd](arkts-form-formobserver-offformadd-f-sys.md#offformadd) |
| [off_formRemove](arkts-form-formobserver-offformremove-f-sys.md#offformremove) |
| [off_message](arkts-form-formobserver-offmessage-f-sys.md#offmessage) |
| [off_notifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md#offnotifyinvisible) |
| [off_notifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md#offnotifyvisible) |
| [off_router](arkts-form-formobserver-offrouter-f-sys.md#offrouter) |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#oncall) |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#oncall系统接口) |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd) |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd系统接口) |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove) |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove系统接口) |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onmessage) |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onmessage系统接口) |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible) |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible系统接口) |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible) |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible系统接口) |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onrouter) |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onrouter系统接口) |
| [on_call](arkts-form-formobserver-oncall-f-sys.md#oncall) |
| [on_call](arkts-form-formobserver-oncall-f-sys.md#oncall系统接口) |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd) |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd系统接口) |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove) |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove系统接口) |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md#onmessage) |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md#onmessage系统接口) |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible) |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible系统接口) |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible) |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible系统接口) |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md#onrouter) |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md#onrouter系统接口) |
<!--DelEnd-->
