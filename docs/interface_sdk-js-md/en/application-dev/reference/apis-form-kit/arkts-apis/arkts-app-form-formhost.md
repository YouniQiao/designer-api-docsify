# @ohos.app.form.formHost

The **formHost** module provides APIs related to the widget host, which is an application that displays the widget content and controls the position where the widget is displayed. You can use the APIs to delete, release, and update widgets installed by the same user, and obtain widget information and status.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md) |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md) |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md) |
| [addForm](arkts-form-formhost-addform-f-sys.md) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md) |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md) |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md) |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md) |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md) |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md) |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md) |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md) |
| [getAllTemplateFormsInfo](arkts-form-formhost-getalltemplateformsinfo-f-sys.md) |
| [getFormIdsByFormLocation](arkts-form-formhost-getformidsbyformlocation-f-sys.md) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md) |
| [getTemplateFormsInfo](arkts-form-formhost-gettemplateformsinfo-f-sys.md) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md) |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md) |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md) |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md) |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md) |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md) |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md) |
| [off](arkts-form-formhost-off-f-sys.md#offformuninstall) |
| [off](arkts-form-formhost-off-f-sys.md#offformoverflow) |
| [off](arkts-form-formhost-off-f-sys.md#offchangesceneanimationstate) |
| [off](arkts-form-formhost-off-f-sys.md#offgetformrect) |
| [off](arkts-form-formhost-off-f-sys.md#offgetliveformstatus) |
| [offChangeSceneAnimationState](arkts-form-formhost-offchangesceneanimationstate-f-sys.md) |
| [offDeleteFormsCallback](arkts-form-formhost-offdeleteformscallback-f-sys.md) |
| [offFormOverflow](arkts-form-formhost-offformoverflow-f-sys.md) |
| [offFormUninstall](arkts-form-formhost-offformuninstall-f-sys.md) |
| [offGetFormRect](arkts-form-formhost-offgetformrect-f-sys.md) |
| [offGetLiveFormStatus](arkts-form-formhost-offgetliveformstatus-f-sys.md) |
| [offGetWantParamsCallback](arkts-form-formhost-offgetwantparamscallback-f-sys.md) |
| [offTemplateFormDetailInfoChange](arkts-form-formhost-offtemplateformdetailinfochange-f-sys.md) |
| [offUpdateFormsConfigCallback](arkts-form-formhost-offupdateformsconfigcallback-f-sys.md) |
| [on](arkts-form-formhost-on-f-sys.md#onformuninstall) |
| [on](arkts-form-formhost-on-f-sys.md#onformoverflow) |
| [on](arkts-form-formhost-on-f-sys.md#onchangesceneanimationstate) |
| [on](arkts-form-formhost-on-f-sys.md#ongetformrect) |
| [on](arkts-form-formhost-on-f-sys.md#ongetliveformstatus) |
| [onChangeSceneAnimationState](arkts-form-formhost-onchangesceneanimationstate-f-sys.md) |
| [onDeleteFormsCallback](arkts-form-formhost-ondeleteformscallback-f-sys.md) |
| [onFormOverflow](arkts-form-formhost-onformoverflow-f-sys.md) |
| [onFormUninstall](arkts-form-formhost-onformuninstall-f-sys.md) |
| [onGetFormRect](arkts-form-formhost-ongetformrect-f-sys.md) |
| [onGetLiveFormStatus](arkts-form-formhost-ongetliveformstatus-f-sys.md) |
| [onGetWantParamsCallback](arkts-form-formhost-ongetwantparamscallback-f-sys.md) |
| [onTemplateFormDetailInfoChange](arkts-form-formhost-ontemplateformdetailinfochange-f-sys.md) |
| [onUpdateFormsConfigCallback](arkts-form-formhost-onupdateformsconfigcallback-f-sys.md) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md) |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md) |
| [recycleForms](arkts-form-formhost-recycleforms-f-sys.md) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md) |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md) |
| [requestForm](arkts-form-formhost-requestform-f-sys.md) |
| [requestFormWithParams](arkts-form-formhost-requestformwithparams-f-sys.md) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md) |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md) |
| [setPublishFormResult](arkts-form-formhost-setpublishformresult-f-sys.md) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md) |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md) |
| [shareForm](arkts-form-formhost-shareform-f-sys.md) |
| [updateFormLocation](arkts-form-formhost-updateformlocation-f-sys.md) |
| [updateFormLockedState](arkts-form-formhost-updateformlockedstate-f-sys.md) |
| [updateFormSize](arkts-form-formhost-updateformsize-f-sys.md) |
<!--DelEnd-->
