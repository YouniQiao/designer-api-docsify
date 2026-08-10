# @ohos.app.form.formObserver

Interface of formObserver.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace formObserver--><!--Device-unnamed-declare namespace formObserver-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { formObserver } from 'kits/@kit.FormKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid-1) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid-2) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid-3) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos-1) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos-2) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos-3) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getrunningforminfosbyfilter) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getrunningforminfosbyfilter-1) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [off](arkts-form-formobserver-off-f-sys.md#off) | Cancels listening to the event of add form.&lt;p&gt;You can use this method to cancel listening to the event of add form.&lt;/p&gt; |
| [off](arkts-form-formobserver-off-f-sys.md#off-1) | Cancels listening to the event of remove form.&lt;p&gt;You can use this method to cancel listening to the event of remove form.&lt;/p&gt; |
| [off](arkts-form-formobserver-off-f-sys.md#off-2) | Cancels listening to the event of notifyVisible type change.&lt;p&gt;You can use this method to cancel listening to the event of notifyVisible type change.&lt;/p&gt; |
| [off](arkts-form-formobserver-off-f-sys.md#off-3) | Cancels listening to the event of notifyInvisible type change.&lt;p&gt;You can use this method to cancel listening to the event of notifyInvisible type change.&lt;/p&gt; |
| [off](arkts-form-formobserver-off-f-sys.md#off-4) | Unregister form router event Listening. |
| [off](arkts-form-formobserver-off-f-sys.md#off-5) | Unregister form message event Listening. |
| [off](arkts-form-formobserver-off-f-sys.md#off-6) | Unregister form call event Listening. |
| [offCall](arkts-form-formobserver-offcall-f-sys.md#offcall) | Unregister form call event Listening. |
| [offFormAdd](arkts-form-formobserver-offformadd-f-sys.md#offformadd) | Cancels listening to the event of add form.&lt;p&gt;You can use this method to cancel listening to the event of add form.&lt;/p&gt; |
| [offFormRemove](arkts-form-formobserver-offformremove-f-sys.md#offformremove) | Cancels listening to the event of remove form.&lt;p&gt;You can use this method to cancel listening to the event of remove form.&lt;/p&gt; |
| [offMessage](arkts-form-formobserver-offmessage-f-sys.md#offmessage) | Unregister form message event Listening. |
| [offNotifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md#offnotifyinvisible) | Cancels listening to the event of notifyInvisible type change.&lt;p&gt;You can use this method to cancel listening to the event of notifyInvisible type change.&lt;/p&gt; |
| [offNotifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md#offnotifyvisible) | Cancels listening to the event of notifyVisible type change.&lt;p&gt;You can use this method to cancel listening to the event of notifyVisible type change.&lt;/p&gt; |
| [offRouter](arkts-form-formobserver-offrouter-f-sys.md#offrouter) | Unregister form router event Listening. |
| [on](arkts-form-formobserver-on-f-sys.md#on) | Listens to the event of add form.&lt;p&gt;You can use this method to listen to the event of add form.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-1) | Listens to the event of add form.&lt;p&gt;You can use this method to listen to the event of add form for a particular card host.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-2) | Listens to the event of remove form.&lt;p&gt;You can use this method to listen to the event of remove form.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-3) | Listens to the event of remove form.&lt;p&gt;You can use this method to listen to the event of remove form for a particular card host.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-4) | Listens to the event of notifyVisible type change.&lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-5) | Listens to the event of notifyVisible type change.&lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-6) | Listens to the event of notifyInvisible type change.&lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-7) | Listens to the event of notifyInvisible type change.&lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-8) | Router event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-9) | Router event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-10) | Message event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-11) | Message event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-12) | Call event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on](arkts-form-formobserver-on-f-sys.md#on-13) | Call event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#oncall) | Call event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#oncall-1) | Call event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd) | Listens to the event of add form.&lt;p&gt;You can use this method to listen to the event of add form.&lt;/p&gt; |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd-1) | Listens to the event of add form.&lt;p&gt;You can use this method to listen to the event of add form for a particular card host.&lt;/p&gt; |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove) | Listens to the event of remove form.&lt;p&gt;You can use this method to listen to the event of remove form.&lt;/p&gt; |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove-1) | Listens to the event of remove form.&lt;p&gt;You can use this method to listen to the event of remove form for a particular card host.&lt;/p&gt; |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onmessage) | Message event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onmessage-1) | Message event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible) | Listens to the event of notifyInvisible type change.&lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt; |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible-1) | Listens to the event of notifyInvisible type change.&lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt; |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible) | Listens to the event of notifyVisible type change.&lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt; |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible-1) | Listens to the event of notifyVisible type change.&lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt; |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onrouter) | Router event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onrouter-1) | Router event listening in registered form.&lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
<!--DelEnd-->

