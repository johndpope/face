#!/usr/bin/env python3
""" The master faceswap.py script """
import gettext
import sys

from lib.cli import args as cli_args
from lib.config import generate_configs
from lib.utils import get_backend


# LOCALES
_LANG = gettext.translation("faceswap", localedir="locales", fallback=True)
_ = _LANG.gettext


if sys.version_info < (3, 7):
    raise Exception("This program requires at least python3.7")
if get_backend() == "amd" and sys.version_info >= (3, 9):
    raise Exception("The AMD version of Faceswap cannot run on versions of Python higher than 3.8")


_PARSER = cli_args.FullHelpArgumentParser()


def _bad_args(*args) -> None:  # pylint:disable=unused-argument
    """ Print help to console when bad arguments are provided. """
    print(cli_args)
    _PARSER.print_help()
    sys.exit(0)


def _main() -> None:
    """ The main entry point into Faceswap.

    - Generates the config files, if they don't pre-exist.
    - Compiles the :class:`~lib.cli.args.FullHelpArgumentParser` objects for each section of
      Faceswap.
    - Sets the default values and launches the relevant script.
    - Outputs help if invalid parameters are provided.
    """
    generate_configs()

    subparser = _PARSER.add_subparsers()
    cli_args.ExtractArgs(subparser, "extract", _("Extract the faces from pictures or a video"))
    cli_args.TrainArgs(subparser, "train", _("Train a model for the two faces A and B"))
    cli_args.ConvertArgs(subparser,
                         "convert",
                         _("Convert source pictures or video to a new one with the face swapped"))
    cli_args.GuiArgs(subparser, "gui", _("Launch the Faceswap Graphical User Interface"))
    _PARSER.set_defaults(func=_bad_args)
    arguments = _PARSER.parse_args()
    arguments.func(arguments)


if __name__ == "__main__":
    _main()
    
  






<!DOCTYPE html>
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">



  <link crossorigin="anonymous" media="all" integrity="sha512-UXiu4O52iBFkqt6Kx5t+pqHYP2/LWWIw9+l5ia74TWw+xPzpH44BFfAQp7yzCe0XFGZa72Xiqyml6tox1KkUjw==" rel="stylesheet" href="https://github.githubassets.com/assets/light-5178aee0ee76.css" /><link crossorigin="anonymous" media="all" integrity="sha512-IX1PnI5wWBz8Kgb1JI0f2QFa/WuRQQHJHe0vkKinQzsxRlNb4b8NgODX5htSZVAAkA1O6Vch+RRlDTI8j96slA==" rel="stylesheet" href="https://github.githubassets.com/assets/dark-217d4f9c8e70.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" integrity="sha512-Ct+ijw5ofrvpiRNwv+EhmU4CBCIgm7ApMfRCT8IQK4luRFZf8tLg0CC0VLyTPVLgMbQ9+74znLAZwi1RSzjpiA==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-0adfa28f0e68.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" integrity="sha512-HIV1s2ZEVz1WLyBRua8znQozNKaQ0LM5AHRX9sMlitm5TNY3QMJzKsRD5FPCF9oluzIXNO9JxRK4bBjxGhcctA==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-1c8575b36644.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" integrity="sha512-URPSviCw4m4n71IKn4qyu7MEDpGbCiTfsMTNrUjPwcg38KtEKDt12vzjlNzoy3YDFiQ8D0TCCYKCtrZpqX097g==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-5113d2be20b0.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" integrity="sha512-yWrddCSE7sqLZ4iqcSOoAsVnCbxs4IgN+oDKgxarp3O6V9dQ8XKyE+ffedHQa55VkB1tY0iNI3QqACG8p1k8IA==" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-c96add742484.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" integrity="sha512-KQ+S9ehnvP9vzfiaBA1FbrSWS1RuJBo/ez+bKUm+XKGEMR22w7Oyc712UyVcpYIqpTCTvaaJ3MfeU0x4xPeI+A==" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-290f92f5e867.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" integrity="sha512-zdiPFGv3QFuv1X24wK9Sa7DM3W/It82kehdMBrepjoJJyJyBISVFUJLvMMkvr4uu8j11Rn35dXZiVrN1FNWzGA==" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-cdd88f146bf7.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" integrity="sha512-IXHqDweLGMT47BTl4v+0woPqFAAtkFBeVqg9U/AliukeUyVREIssCu32RfWmXNdMjwmdVBcS+q9SMQMYuYF5dQ==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-2171ea0f078b.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-SUqyEQoqiybF4TGdLH0th4vDL9I9EFGTXfcth9CIVAoNeQJfAyfu8MtmOMWbGnqP6VxFIQ6VdDHxhdXNG1k//Q==" rel="stylesheet" href="https://github.githubassets.com/assets/primer-494ab2110a2a.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-RPD+VCMOYAJt/t3kXPs/XrWUQE2ggPEN39P8G2jSiA6OrHaM//aMgtT8uupQNJdm4mcsUn2vi/ahr6KbYVHUmQ==" rel="stylesheet" href="https://github.githubassets.com/assets/global-44f0fe54230e.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-RF1HM+a5AgDJgMFCxwJx21deB4Rap8Ft/EwcvMN0Ae7iqKyiSDrcSqf7CZ92MLuPDBsItnwlNayP4AUKTRY2GQ==" rel="stylesheet" href="https://github.githubassets.com/assets/github-445d4733e6b9.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-PXtwH8brj9qH7LskWA0iAMLw4Wx3RXN7txSxjlqdzQEalZKu3UcsQ+ajfHJMDkYDA2iWL1FIrf2zyLflA5Xu7A==" rel="stylesheet" href="https://github.githubassets.com/assets/code-3d7b701fc6eb.css" />

    <meta name="optimizely-datafile" content="{&quot;groups&quot;: [], &quot;environmentKey&quot;: &quot;production&quot;, &quot;rollouts&quot;: [], &quot;typedAudiences&quot;: [], &quot;projectId&quot;: &quot;16737760170&quot;, &quot;variables&quot;: [], &quot;featureFlags&quot;: [], &quot;experiments&quot;: [{&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20667381018&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20680930759&quot;, &quot;key&quot;: &quot;treatment&quot;}], &quot;id&quot;: &quot;20652570897&quot;, &quot;key&quot;: &quot;project_genesis&quot;, &quot;layerId&quot;: &quot;20672300363&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20667381018&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20680930759&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;83356e17066d336d1803024138ecb683&quot;: &quot;treatment&quot;, &quot;18e31c8a9b2271332466133162a4aa0d&quot;: &quot;treatment&quot;, &quot;10f8ab3fbc5ebe989a36a05f79d48f32&quot;: &quot;treatment&quot;, &quot;1686089f6d540cd2deeaec60ee43ecf7&quot;: &quot;treatment&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;21427950901&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21429710665&quot;, &quot;key&quot;: &quot;beginner&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21437291543&quot;, &quot;key&quot;: &quot;upstart&quot;}], &quot;id&quot;: &quot;21445030708&quot;, &quot;key&quot;: &quot;_259_zero_user_dashboard&quot;, &quot;layerId&quot;: &quot;21434011841&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;21427950901&quot;, &quot;endOfRange&quot;: 3334}, {&quot;entityId&quot;: &quot;21427950901&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;21427950901&quot;, &quot;endOfRange&quot;: 8333}, {&quot;entityId&quot;: &quot;21427950901&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;3c64268131793aa297119a343c19e345&quot;: &quot;beginner&quot;, &quot;95b24126db31ea8693c0fe5ea9f53b65&quot;: &quot;beginner&quot;, &quot;086e2abe64e9101112af53b95d2d90b9&quot;: &quot;upstart&quot;, &quot;bae688df9d297afac98e2d254e912ada&quot;: &quot;control&quot;, &quot;6c2cfda7c41396fcc31a4db759a42b94&quot;: &quot;beginner&quot;, &quot;16ed2b4ff7de02663b7c606309695916&quot;: &quot;control&quot;, &quot;1971768911.1635962195&quot;: &quot;beginner&quot;, &quot;830bf802470ec6c9c5800c99d8e57445&quot;: &quot;beginner&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;21454052779&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21450922535&quot;, &quot;key&quot;: &quot;redesign&quot;}], &quot;id&quot;: &quot;21486342806&quot;, &quot;key&quot;: &quot;_261_downgrade&quot;, &quot;layerId&quot;: &quot;21478441323&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;21454052779&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;21450922535&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;60c046ae30e9007c321e5539ae1738b5&quot;: &quot;redesign&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;21540260416&quot;, &quot;key&quot;: &quot;variant_fetch_upstream&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21551370594&quot;, &quot;key&quot;: &quot;variant_sync_fork&quot;}], &quot;id&quot;: &quot;21532540507&quot;, &quot;key&quot;: &quot;fork_syncing&quot;, &quot;layerId&quot;: &quot;21510660568&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;21551370594&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;21551370594&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;bcceffdcc63834cc146ddb8cce0c556d&quot;: &quot;variant_sync_fork&quot;, &quot;0bd228f43ec6ac1a9eb9087f4e2471e6&quot;: &quot;variant_sync_fork&quot;, &quot;404ee4d837b290b3089170d9226758ea&quot;: &quot;variant_sync_fork&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;21672251105&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21636601473&quot;, &quot;key&quot;: &quot;primer&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21663911434&quot;, &quot;key&quot;: &quot;growth&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;21673341369&quot;, &quot;key&quot;: &quot;brand&quot;}], &quot;id&quot;: &quot;21685100630&quot;, &quot;key&quot;: &quot;_241_onboard_users_to_protect_branches&quot;, &quot;layerId&quot;: &quot;21696970697&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;21672251105&quot;, &quot;endOfRange&quot;: 825}, {&quot;entityId&quot;: &quot;21636601473&quot;, &quot;endOfRange&quot;: 2310}, {&quot;entityId&quot;: &quot;21636601473&quot;, &quot;endOfRange&quot;: 2500}, {&quot;entityId&quot;: &quot;21636601473&quot;, &quot;endOfRange&quot;: 2830}, {&quot;entityId&quot;: &quot;21636601473&quot;, &quot;endOfRange&quot;: 3135}, {&quot;entityId&quot;: &quot;21636601473&quot;, &quot;endOfRange&quot;: 3310}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 3325}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 3980}, {&quot;entityId&quot;: &quot;21636601473&quot;, &quot;endOfRange&quot;: 3995}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 4170}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 5155}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 5330}, {&quot;entityId&quot;: &quot;21663911434&quot;, &quot;endOfRange&quot;: 5825}, {&quot;entityId&quot;: &quot;21672251105&quot;, &quot;endOfRange&quot;: 6000}, {&quot;entityId&quot;: &quot;21672251105&quot;, &quot;endOfRange&quot;: 7500}, {&quot;entityId&quot;: &quot;21673341369&quot;, &quot;endOfRange&quot;: 7830}, {&quot;entityId&quot;: &quot;21673341369&quot;, &quot;endOfRange&quot;: 8325}, {&quot;entityId&quot;: &quot;21673341369&quot;, &quot;endOfRange&quot;: 9330}, {&quot;entityId&quot;: &quot;21673341369&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;409007617793ebd1e12654adf87047d0&quot;: &quot;growth&quot;, &quot;3977d8a7a265a13d734f3edf9226214c&quot;: &quot;primer&quot;, &quot;bcf588169e3ac842af083a5a54708563&quot;: &quot;growth&quot;}}], &quot;version&quot;: &quot;4&quot;, &quot;audiences&quot;: [{&quot;conditions&quot;: &quot;[\&quot;or\&quot;, {\&quot;match\&quot;: \&quot;exact\&quot;, \&quot;name\&quot;: \&quot;$opt_dummy_attribute\&quot;, \&quot;type\&quot;: \&quot;custom_attribute\&quot;, \&quot;value\&quot;: \&quot;$opt_dummy_value\&quot;}]&quot;, &quot;id&quot;: &quot;$opt_dummy_audience&quot;, &quot;name&quot;: &quot;Optimizely-Generated Audience for Backwards Compatibility&quot;}], &quot;anonymizeIP&quot;: true, &quot;sdkKey&quot;: &quot;WTc6awnGuYDdG98CYRban&quot;, &quot;attributes&quot;: [{&quot;id&quot;: &quot;16822470375&quot;, &quot;key&quot;: &quot;user_id&quot;}, {&quot;id&quot;: &quot;17143601254&quot;, &quot;key&quot;: &quot;spammy&quot;}, {&quot;id&quot;: &quot;18175660309&quot;, &quot;key&quot;: &quot;organization_plan&quot;}, {&quot;id&quot;: &quot;18813001570&quot;, &quot;key&quot;: &quot;is_logged_in&quot;}, {&quot;id&quot;: &quot;19073851829&quot;, &quot;key&quot;: &quot;geo&quot;}, {&quot;id&quot;: &quot;20175462351&quot;, &quot;key&quot;: &quot;requestedCurrency&quot;}, {&quot;id&quot;: &quot;20785470195&quot;, &quot;key&quot;: &quot;country_code&quot;}, {&quot;id&quot;: &quot;21656311196&quot;, &quot;key&quot;: &quot;opened_downgrade_dialog&quot;}], &quot;botFiltering&quot;: false, &quot;accountId&quot;: &quot;16737760170&quot;, &quot;events&quot;: [{&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;17911811441&quot;, &quot;key&quot;: &quot;hydro_click.dashboard.teacher_toolbox_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18124116703&quot;, &quot;key&quot;: &quot;submit.organizations.complete_sign_up&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18145892387&quot;, &quot;key&quot;: &quot;no_metric.tracked_outside_of_optimizely&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18178755568&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.add_repo&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18180553241&quot;, &quot;key&quot;: &quot;submit.repository_imports.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18186103728&quot;, &quot;key&quot;: &quot;click.help.learn_more_about_repository_creation&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18188530140&quot;, &quot;key&quot;: &quot;test_event&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18191963644&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.transfer_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18195612788&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.import_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18210945499&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.invite_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18211063248&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.create_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18215721889&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.update_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18224360785&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.dismiss&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18234832286&quot;, &quot;key&quot;: &quot;submit.organization_activation.complete&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18252392383&quot;, &quot;key&quot;: &quot;submit.org_repository.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18257551537&quot;, &quot;key&quot;: &quot;submit.org_member_invitation.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18259522260&quot;, &quot;key&quot;: &quot;submit.organization_profile.update&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18564603625&quot;, &quot;key&quot;: &quot;view.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18568612016&quot;, &quot;key&quot;: &quot;click.classroom_sign_in_click&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18572592540&quot;, &quot;key&quot;: &quot;view.classroom_name&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18574203855&quot;, &quot;key&quot;: &quot;click.classroom_create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18582053415&quot;, &quot;key&quot;: &quot;click.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18589463420&quot;, &quot;key&quot;: &quot;click.classroom_create_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591323364&quot;, &quot;key&quot;: &quot;click.classroom_create_first_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591652321&quot;, &quot;key&quot;: &quot;click.classroom_grant_access&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18607131425&quot;, &quot;key&quot;: &quot;view.classroom_creation&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18831680583&quot;, &quot;key&quot;: &quot;upgrade_account_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19064064515&quot;, &quot;key&quot;: &quot;click.signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19075373687&quot;, &quot;key&quot;: &quot;click.view_account_billing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19077355841&quot;, &quot;key&quot;: &quot;click.dismiss_signup_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19079713938&quot;, &quot;key&quot;: &quot;click.contact_sales&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19120963070&quot;, &quot;key&quot;: &quot;click.compare_account_plans&quot;}, {&quot;experimentIds&quot;: [&quot;21685100630&quot;], &quot;id&quot;: &quot;19151690317&quot;, &quot;key&quot;: &quot;click.upgrade_account_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19424193129&quot;, &quot;key&quot;: &quot;click.open_account_switcher&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19520330825&quot;, &quot;key&quot;: &quot;click.visit_account_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19540970635&quot;, &quot;key&quot;: &quot;click.switch_account_context&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19730198868&quot;, &quot;key&quot;: &quot;submit.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19820830627&quot;, &quot;key&quot;: &quot;click.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19988571001&quot;, &quot;key&quot;: &quot;click.create_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20036538294&quot;, &quot;key&quot;: &quot;click.create_organization_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20040653299&quot;, &quot;key&quot;: &quot;click.input_enterprise_trial_form&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20062030003&quot;, &quot;key&quot;: &quot;click.continue_with_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20068947153&quot;, &quot;key&quot;: &quot;click.create_organization_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20086636658&quot;, &quot;key&quot;: &quot;click.signup_continue.username&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20091648988&quot;, &quot;key&quot;: &quot;click.signup_continue.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20103637615&quot;, &quot;key&quot;: &quot;click.signup_continue.email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20111574253&quot;, &quot;key&quot;: &quot;click.signup_continue.password&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20120044111&quot;, &quot;key&quot;: &quot;view.pricing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20152062109&quot;, &quot;key&quot;: &quot;submit.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20165800992&quot;, &quot;key&quot;: &quot;submit.upgrade_payment_form&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20171520319&quot;, &quot;key&quot;: &quot;submit.create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20222645674&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.discuss_your_needs&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20227443657&quot;, &quot;key&quot;: &quot;submit.verify_primary_user_email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20234607160&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.try_enterprise&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20238175784&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20239847212&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.continue_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20251097193&quot;, &quot;key&quot;: &quot;recommended_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20438619534&quot;, &quot;key&quot;: &quot;click.pricing_calculator.1_member&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20456699683&quot;, &quot;key&quot;: &quot;click.pricing_calculator.15_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20467868331&quot;, &quot;key&quot;: &quot;click.pricing_calculator.10_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20476267432&quot;, &quot;key&quot;: &quot;click.trial_days_remaining&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20476357660&quot;, &quot;key&quot;: &quot;click.discover_feature&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20479287901&quot;, &quot;key&quot;: &quot;click.pricing_calculator.custom_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20481107083&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.apply_teacher_benefits&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20483089392&quot;, &quot;key&quot;: &quot;click.pricing_calculator.5_members&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20484283944&quot;, &quot;key&quot;: &quot;click.onboarding_task&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20484996281&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.apply_student_benefits&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20486713726&quot;, &quot;key&quot;: &quot;click.onboarding_task_breadcrumb&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20490791319&quot;, &quot;key&quot;: &quot;click.upgrade_to_enterprise&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20491786766&quot;, &quot;key&quot;: &quot;click.talk_to_us&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20494144087&quot;, &quot;key&quot;: &quot;click.dismiss_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20499722759&quot;, &quot;key&quot;: &quot;completed_all_tasks&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20500710104&quot;, &quot;key&quot;: &quot;completed_onboarding_tasks&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20513160672&quot;, &quot;key&quot;: &quot;click.read_doc&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20516196762&quot;, &quot;key&quot;: &quot;actions_enabled&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20518980986&quot;, &quot;key&quot;: &quot;click.dismiss_trial_banner&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20535446721&quot;, &quot;key&quot;: &quot;click.issue_actions_prompt.dismiss_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20557002247&quot;, &quot;key&quot;: &quot;click.issue_actions_prompt.setup_workflow&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20595070227&quot;, &quot;key&quot;: &quot;click.pull_request_setup_workflow&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20626600314&quot;, &quot;key&quot;: &quot;click.seats_input&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20642310305&quot;, &quot;key&quot;: &quot;click.decrease_seats_number&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20662990045&quot;, &quot;key&quot;: &quot;click.increase_seats_number&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20679620969&quot;, &quot;key&quot;: &quot;click.public_product_roadmap&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20761240940&quot;, &quot;key&quot;: &quot;click.dismiss_survey_banner&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20767210721&quot;, &quot;key&quot;: &quot;click.take_survey&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20795281201&quot;, &quot;key&quot;: &quot;click.archive_list&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20966790249&quot;, &quot;key&quot;: &quot;contact_sales.submit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20996500333&quot;, &quot;key&quot;: &quot;contact_sales.existing_customer&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20996890162&quot;, &quot;key&quot;: &quot;contact_sales.blank_message_field&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21000470317&quot;, &quot;key&quot;: &quot;contact_sales.personal_email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21002790172&quot;, &quot;key&quot;: &quot;contact_sales.blank_phone_field&quot;}, {&quot;experimentIds&quot;: [&quot;21445030708&quot;], &quot;id&quot;: &quot;21354412592&quot;, &quot;key&quot;: &quot;click.dismiss_create_readme&quot;}, {&quot;experimentIds&quot;: [&quot;21445030708&quot;], &quot;id&quot;: &quot;21366102546&quot;, &quot;key&quot;: &quot;click.dismiss_zero_user_content&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21370252505&quot;, &quot;key&quot;: &quot;account_did_downgrade&quot;}, {&quot;experimentIds&quot;: [&quot;21445030708&quot;], &quot;id&quot;: &quot;21370840408&quot;, &quot;key&quot;: &quot;click.cta_create_readme&quot;}, {&quot;experimentIds&quot;: [&quot;21445030708&quot;], &quot;id&quot;: &quot;21375451068&quot;, &quot;key&quot;: &quot;click.cta_create_new_repository&quot;}, {&quot;experimentIds&quot;: [&quot;21445030708&quot;], &quot;id&quot;: &quot;21385390948&quot;, &quot;key&quot;: &quot;click.zero_user_content&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21467712175&quot;, &quot;key&quot;: &quot;click.downgrade_keep&quot;}, {&quot;experimentIds&quot;: [&quot;21486342806&quot;], &quot;id&quot;: &quot;21484112202&quot;, &quot;key&quot;: &quot;click.downgrade&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21495292213&quot;, &quot;key&quot;: &quot;click.downgrade_survey_exit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21508241468&quot;, &quot;key&quot;: &quot;click.downgrade_survey_submit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21512030356&quot;, &quot;key&quot;: &quot;click.downgrade_support&quot;}, {&quot;experimentIds&quot;: [&quot;21486342806&quot;], &quot;id&quot;: &quot;21539090022&quot;, &quot;key&quot;: &quot;click.downgrade_exit&quot;}, {&quot;experimentIds&quot;: [&quot;21532540507&quot;], &quot;id&quot;: &quot;21543640644&quot;, &quot;key&quot;: &quot;click_fetch_upstream&quot;}, {&quot;experimentIds&quot;: [&quot;21685100630&quot;], &quot;id&quot;: &quot;21646510300&quot;, &quot;key&quot;: &quot;click.move_your_work&quot;}, {&quot;experimentIds&quot;: [&quot;21685100630&quot;], &quot;id&quot;: &quot;21656151116&quot;, &quot;key&quot;: &quot;click.add_branch_protection_rule&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21663860599&quot;, &quot;key&quot;: &quot;click.downgrade_dialog_open&quot;}, {&quot;experimentIds&quot;: [&quot;21685100630&quot;], &quot;id&quot;: &quot;21687860483&quot;, &quot;key&quot;: &quot;click.learn_about_protected_branches&quot;}, {&quot;experimentIds&quot;: [&quot;21685100630&quot;], &quot;id&quot;: &quot;21689050333&quot;, &quot;key&quot;: &quot;click.dismiss_protect_this_branch&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21864370109&quot;, &quot;key&quot;: &quot;click.sign_in&quot;}], &quot;revision&quot;: &quot;1338&quot;}" />


  <script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-J+x3va0bRTq/ai4jj6xgn73qFfgtAlc00uA3LFZaGWRBSPh+sz0AVQvjSl1Dhgg+nhRjEA9W4C6hyo2KIPfW3w==" src="https://github.githubassets.com/assets/runtime-27ec77bdad1b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-ivm676uepRn1vQvL/mShZVrbNfsUUZRp0a2RCZNYrFJYFlYhdDU2P+UC8axgVT17oqv1BVQLngSsGoiBN2MJpw==" src="https://github.githubassets.com/assets/vendors-node_modules_manuelpuyol_turbo_dist_turbo_es2017-esm_js-8af9baefab9e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-GB4jwt8fni2MoE1wzROiGvrgScSHotjr1A9c1FQKUTsfuFn9W2y5/knx+uD8eOAC1rVSA3UPi3h+PTwAuaDZYQ==" src="https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-181e23c2df1f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-2SerPrWVdwzHS5122vJBgSSpm90BG2FuGQKBap/Qj4Vi975I1t9e5V0JQ5AGkoZmuK+NNr79TD7OUN9A+Y1t6w==" src="https://github.githubassets.com/assets/environment-d927ab3eb595.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-ZQM3kW293O7WR1cDuHZ02wendjejLzwVD0wy4L1eCNr34RHXiY05wmHUx4hnV9WELD/OEZRGrzK+M8uwiZ/WEw==" src="https://github.githubassets.com/assets/vendors-node_modules_selector-observer_dist_index_esm_js-650337916dbd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-Si8390GeCVPslYj8WomaMCyj33Jutd8vZ+Sdi6WXLSbdZRyC4wwijhTNyLy0zpHhfYnrynP6qArdz1PXti1sOg==" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-63debe-4a2f37f7419e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-IW3JseO0m0yclixsxDwuXBlAp0+bXVZkAzcVRd5lkCD0Ue980eWiIMfA6uj69EXXq3KwhHWewR3/HTeR+v5G8A==" src="https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-c7e9ed-216dc9b1e3b4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-OMNqWXGEHws0bOVmDm9Nau8e8ZrjKUF77hq8heNd45JYuDu+gm4tZhYB/bUbysfBQ/6y31S1R0VIpjOHiCotUA==" src="https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_time-elements_dist_index_js-38c36a597184.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-0spbqRlGZ/7LnB7VMP6g5uqkJ2V+2QYrLwsoRQ98Vvw6NZuSEaqs+VvZ2AKpTj20Jv336D4Z9Ue6koMWnTzCXg==" src="https://github.githubassets.com/assets/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_github_mark-f079ea-d2ca5ba91946.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-RGVcB6gZf6KXgW6ybbWo6x51i6+qFg7hVO5EvlPdYWzQYpjrF5qym7/xQaIvRUFC2y7kCX5y2xg04lpZ21Dkhg==" src="https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-b3d32f-44655c07a819.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-VIfOunBprhUcFctmrXIqpc9faEITK2Fj1kmg+v814LcciwMkpaa0PvP8dbISOF7MQFHCRXzoseSpH0KlStRcbQ==" src="https://github.githubassets.com/assets/github-elements-5487ceba7069.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-snnd8i/F+EVdq0ZXEo2TWNgS7zIIBa6w1uAQBQ0V/tkW+jZEsU+zfmCwugV3nchvm3cGBGcSduJRWMvVBG4SSw==" src="https://github.githubassets.com/assets/element-registry-b279ddf22fc5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-6VTowByTC7C1Ae4nuESJ5iT76vchmVCzjuit7IR83B/TPkwjSserSlr83SYhLvIfNLvJfB2zH0bHBr8+fzIa+w==" src="https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-e954e8c01c93.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-3YkTrGWwrb2whIVWEwKEhghL4yI2UAHnLW/QtnYMQFLkfQUYD3gtJ2WqDJg8wzzSm0rP05KFDOsKKx4a1wQRdA==" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_hotkey_dist_index-9f48bd-dd8913ac65b0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-YlZzfDs0sJwb4LDPoYGzppaasG/yvY8DolVk64u7Kjpyz/NpKS3E7toBkHcDxNSB8x7mlDDjC2nHuWiltsMGvQ==" src="https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_github_catalyst_lib_index_-bd1f73-6256737c3b34.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-V4+K12am3OXCOQYegHoAFHR3Y4Zy9u97+gR5aLOTVia3tTeNPe39FlKnvnwjndeuEOWfkzXKB2iL2UwOKOZM+g==" src="https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_koddsson_textarea-c-586f78-578f8ad766a6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-VY2CzuSOZRicBEh6k2l9QSBhAi9ZDNjxREDsYUHzzVMK/cJDyb40PYTGQuAhrNZh69oAo3ap8ZEwaAJxeX6TOg==" src="https://github.githubassets.com/assets/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-1c1fef-558d82cee48e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-iv5zc66CDnM+oVHCDv7cko+Bee6Q895DqJ52+TvMOtDYiEWLpTjQheRSbAygXr1SdVa7CSDLpnj3ze+dv1eIaw==" src="https://github.githubassets.com/assets/app_assets_modules_github_soft-nav_navigate_ts-8afe7373ae82.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-KD3D2b33I5qaAa+WTVFFwYVEJ8IU3yIPmJzm7DJz/4EXR77iHpG/FmALojXov3metaa41+XcrQKAf1e5iBmFWw==" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_keyboard-shortcuts-helper_ts-app_assets_modules_github_di-9b8a64-283dc3d9bdf7.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-sFfyQjq1ObFkfG0l+z9HzzoSicV7DnX6adtbhmwkcwapEIZkJef1OWQl3cYK14uRj/DZcMBTf9630E9xIyxDeA==" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_has-interactions_t-0091d6-b057f2423ab5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-2/yZbbsa0eoF4BF8AKcHb9138TwEo5Rut7Y4qccJG6jw743B22M0oxT//bBs1CM9bTUqN3OAMf4k2mFl4+oYEQ==" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_details_ts-app_assets_modules_github_behaviors_include-fr-29e9d6-dbfc996dbb1a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-23lZtf/52z40ONnc8LqhXQ+V9egvurRHmvCUvgTJffdld26nI1WnOdt/T/cS10mOmyOYXMCh8EC+UgMrnENNXg==" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-db7959b5fff9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-v0joQDPyLFGfsOGbuW+o4K9FNN1EeXwzl03KD0m85qoYZfdL6hPsANi/MzBjLX3xdSolrf+uvQaYw2yIjo02Gg==" src="https://github.githubassets.com/assets/behaviors-bf48e84033f2.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-sBMWdU4gNYQCipbJqsK4SMltTx7u8+15gnwz2Ag8mncGk+kYYyNHGr5eESzm5qp3aYfrYNaglenhEM4lIktOhw==" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-06ff533-b01316754e20.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-R7o1000dzeCE1mcYw+5zqKJlpzHvN84vPKJNcySE14vOICRT/0mpRTeZ1guSksLNZFDrQE58mpt4/wJSn03Gtw==" src="https://github.githubassets.com/assets/notifications-global-47ba35d34d1d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-zJei4l6VynbbZLG3C4JZilhEZt1EJ/LeWP+Q7zEI0YsrLdu1L1rb1FU9zAvh+UBlY1xdiWuPpMTvh1VXzZWmYQ==" src="https://github.githubassets.com/assets/vendors-node_modules_optimizely_optimizely-sdk_dist_optimizely_browser_es_min_js-node_modules-089adc-cc97a2e25e95.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-WosXOLIgGiylocEf5wY0P/R77ob+y8I/5diEbAFE/j6B0PV+SaTXO/rH7iLQmx5jLzyeIcTljwlrvCtSD9mlmg==" src="https://github.githubassets.com/assets/optimizely-5a8b1738b220.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-F8z8SSakEr7YpDXzZGEdriFwg9sCN9ptY7hKHSZowNV10rNMr5Ihp5qxYkZxWMPrmXulB8ra4tuxEPpZdMNbeg==" src="https://github.githubassets.com/assets/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-17ccfc4926a4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-oAlX0XR56505HI88EmHkjEDFG0d2Ls5ieGCbgUeQziMOCpSrFJD4rvFCn3CJxo2zBiGXGNhiaf/8JdYUJIiKkw==" src="https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-911b971-a00957d17479.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-P8gAs7JrEJtCSAwGpwjY8QXeiTtsEeWeKYFDXlEgwIv86lnd6Ji9//3mpEbVgj0dQoUxwjHCP9I2mJqw42SiKQ==" src="https://github.githubassets.com/assets/app_assets_modules_github_ref-selector_ts-3fc800b3b26b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-EN7AtPbOCCKfKfz7rdaUSsJUf04y5T6dsgpXfZBi115bwLAwiqzsgXdUGNWe1bj+3iHsY9xuB7muZqQ8oUg1hA==" src="https://github.githubassets.com/assets/codespaces-10dec0b4f6ce.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-ptYtfjzCdht+Xw7VxgISCposRVgYuQwr6IJx0gr+DLSKdiLigWZ6RTP//Dkdlv/axEyOzSI9XiW0zLsrdLTv8Q==" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_github_remote-form_-65a541-a6d62d7e3cc2.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-f/7QW6/re871sCPOZwb8QNzGxl95Rf95am57+GCVvdeTTo01dfEe7rZg2Dz6DOmxcaRSbQtsLGo29u5mT+XqcQ==" src="https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_filter--8b2f15-7ffed05bafeb.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-1MYse4cJP0zg9qMSsPaEdT7wAUlaFg7uAQm7HbriQh0Fmx9aDR879nB7aRz4KI0fx6HRIIoi9dCUHFLlU6fsiA==" src="https://github.githubassets.com/assets/repositories-d4c62c7b8709.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-2rS2mk8k3nqrfOmfAECK35UWWuKwh1v/JSXks5IRy9YaQMAwiqzXphHYAe0KKPXIAUHH/1ByRuBOMEKgmicwpw==" src="https://github.githubassets.com/assets/topic-suggestions-dab4b69a4f24.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-BbIYbSNANE5qMpaxgHK9AW2Vis2F2i7q6+UMvDcIKqHm+XTwFB5p/TP3/hoywD1NRUTNwV52uLyLqHQvNtGVGA==" src="https://github.githubassets.com/assets/code-menu-05b2186d2340.js"></script>
  

  <title>GitHub - borisdayma/faceswap: Deepfakes Software For All</title>



    

  <meta name="request-id" content="F58B:26A2:57A52E:9339AE:62FBCDBA" data-pjax-transient="true"/><meta name="html-safe-nonce" content="ce869aceb9dab838cc9ff25868dd0186e880942df12cc76fd814fa0d5467999f" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJGNThCOjI2QTI6NTdBNTJFOjkzMzlBRTo2MkZCQ0RCQSIsInZpc2l0b3JfaWQiOiI0NTk0NTk4Mzg1MzI2NjUxMTg2IiwicmVnaW9uX2VkZ2UiOiJpYWQiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-pjax-transient="true"/><meta name="visitor-hmac" content="5538b99bed72d4d4a18a0169586f2c59b02d0ceb13847d69afb73efcf32193de" data-pjax-transient="true"/>

    <meta name="hovercard-subject-tag" content="repository:211183970" data-pjax-transient>


  <meta name="github-keyboard-shortcuts" content="repository" data-pjax-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-pjax-transient="true" />

  




  

    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">
    
      <meta name="description" content="Deepfakes Software For All. Contribute to borisdayma/faceswap development by creating an account on GitHub.">
      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905" />
      <meta name="twitter:image:src" content="https://opengraph.githubassets.com/262c2076eda025c0ec8a92790c9298e998b094424e3df6560a7e054afc8af412/borisdayma/faceswap" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="GitHub - borisdayma/faceswap: Deepfakes Software For All" /><meta name="twitter:description" content="Deepfakes Software For All. Contribute to borisdayma/faceswap development by creating an account on GitHub." />
      <meta property="og:image" content="https://opengraph.githubassets.com/262c2076eda025c0ec8a92790c9298e998b094424e3df6560a7e054afc8af412/borisdayma/faceswap" /><meta property="og:image:alt" content="Deepfakes Software For All. Contribute to borisdayma/faceswap development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="GitHub - borisdayma/faceswap: Deepfakes Software For All" /><meta property="og:url" content="https://github.com/borisdayma/faceswap" /><meta property="og:description" content="Deepfakes Software For All. Contribute to borisdayma/faceswap development by creating an account on GitHub." />
      
    <link rel="assets" href="https://github.githubassets.com/">


        <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">

    <meta name="enabled-features" content="IMAGE_METRIC_TRACKING,GEOJSON_AZURE_MAPS">


  <meta http-equiv="x-pjax-version" content="25b57c36bfd1de1675987aa63be8a09479bc84555f80edca63916ac2a6aca36f" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="d36423f9dec35f40d75bda7103dfcd1e46c44bd6aac49a971abe9919b3354f73" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="acec35236a7fd7dd95fe6939db3dc1ab506e500c0b068672aa1b5d813668a687" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="c45fdfd625f12e835bafa7cc4c8e66eef93efe61f1ac5f8d33b571f2e631db9c" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-pjax-transient="">

    
  <meta name="go-import" content="github.com/borisdayma/faceswap git https://github.com/borisdayma/faceswap.git">

  <meta name="octolytics-dimension-user_id" content="715491" /><meta name="octolytics-dimension-user_login" content="borisdayma" /><meta name="octolytics-dimension-repository_id" content="211183970" /><meta name="octolytics-dimension-repository_nwo" content="borisdayma/faceswap" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="true" /><meta name="octolytics-dimension-repository_parent_id" content="114747226" /><meta name="octolytics-dimension-repository_parent_nwo" content="deepfakes/faceswap" /><meta name="octolytics-dimension-repository_network_root_id" content="114747226" /><meta name="octolytics-dimension-repository_network_root_nwo" content="deepfakes/faceswap" />



    <link rel="canonical" href="https://github.com/borisdayma/faceswap" data-pjax-transient>
  <meta name="turbo-body-classes" content="logged-out env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive" style="word-wrap: break-word;">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader js-pjax-loader-bar Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


        

            <script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-QXIxqYUlWaXrcdN4cHQlC5KXn2kLBmHHRGsR9I8V663O/bmVvt+hQVH2G6R2rttQ9EshUvuGIDdGQkVH4OA/8w==" src="https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-417231a98525.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" integrity="sha512-MZCSrz0zsvcOl7aWH/U2sbVkQxfQHqMzLn7XCqqpA5yRhkPoC2u8aQ9pOuNezZVhEOIGms8DNg7V1+iwijR3lA==" src="https://github.githubassets.com/assets/sessions-319092af3d33.js"></script>
<header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
  <div class="container-xl d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
      <a class="mr-4 color-fg-inherit" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
        <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
      </a>

        <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
          

        </div>

      <div class="d-flex flex-items-center">
            <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&amp;source=header-repo"
              class="d-inline-block d-lg-none f5 no-underline border color-border-default rounded-2 px-2 py-1 mr-3 mr-sm-5 color-fg-inherit"
              data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="7d991fb921c02d035d58993e155ee9da015b5f6bcb33108b81a2d259cc404c8c"
            >
              Sign&nbsp;up
            </a>

          <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target btn-link d-lg-none mt-1 color-fg-inherit">    <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-three-bars">
    <path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path>
</svg>
</button>      </div>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-flex d-lg-none flex-justify-end border-bottom color-bg-subtle p-3">
          <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target btn-link">    <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-x color-fg-muted">
    <path fill-rule="evenodd" d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z"></path>
</svg>
</button>      </div>

        <nav class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0" aria-label="Global">
          <ul class="d-lg-flex list-style-none">
              <li class="mr-0 mr-lg-3 position-relative flex-wrap flex-justify-between flex-items-center border-bottom border-lg-bottom-0 d-block d-lg-flex flex-lg-nowrap flex-lg-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
      <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
        Product
        <svg x="0" y="0" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative"><path d="M1,1l6.2,6L13,1"></path></svg>
      </summary>
      <div class="dropdown-menu flex-auto rounded px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
        <ul class="list-style-none f5 pb-1">
              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--primary text-bold py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Features&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Features;&quot;}" href="/features">
      Features
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Mobile&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Mobile;&quot;}" href="/mobile">
      Mobile
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Actions&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Actions;&quot;}" href="/features/actions">
      Actions
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Codespaces&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Codespaces;&quot;}" href="/features/codespaces">
      Codespaces
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Copilot&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Copilot;&quot;}" href="/features/copilot">
      Copilot
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Packages&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Packages;&quot;}" href="/features/packages">
      Packages
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Security&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Security;&quot;}" href="/features/security">
      Security
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Code review&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Code review;&quot;}" href="/features/code-review">
      Code review
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Issues&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Issues;&quot;}" href="/features/issues">
      Issues
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Discussions&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Discussions;&quot;}" href="/features/discussions">
      Discussions
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Integrations&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Integrations;&quot;}" href="/features/integrations">
      Integrations
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--primary text-bold border-top pt-4 pb-2 mt-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to GitHub Sponsors&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:GitHub Sponsors;&quot;}" href="/sponsors">
      GitHub Sponsors
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--primary text-bold py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Customer stories&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Customer stories;&quot;}" href="/customer-stories">
      Customer stories
</a>  </li>

        </ul>
      </div>
    </details>
</li>


              <li class="mr-0 mr-lg-3 position-relative flex-wrap flex-justify-between flex-items-center border-bottom border-lg-bottom-0 d-block d-lg-flex flex-lg-nowrap flex-lg-items-center">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-analytics-event="{&quot;category&quot;:&quot;Header menu top item (logged out)&quot;,&quot;action&quot;:&quot;click to go to Team&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Team;&quot;}" href="/team">Team</a>
</li>

              <li class="mr-0 mr-lg-3 position-relative flex-wrap flex-justify-between flex-items-center border-bottom border-lg-bottom-0 d-block d-lg-flex flex-lg-nowrap flex-lg-items-center">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-analytics-event="{&quot;category&quot;:&quot;Header menu top item (logged out)&quot;,&quot;action&quot;:&quot;click to go to Enterprise&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Enterprise;&quot;}" href="/enterprise">Enterprise</a>
</li>


            <li class="mr-0 mr-lg-3 position-relative flex-wrap flex-justify-between flex-items-center border-bottom border-lg-bottom-0 d-block d-lg-flex flex-lg-nowrap flex-lg-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
      <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
        Explore
        <svg x="0" y="0" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative"><path d="M1,1l6.2,6L13,1"></path></svg>
      </summary>
      <div class="dropdown-menu flex-auto rounded px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
        <ul class="list-style-none f5 pb-1">
              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--primary text-bold py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Explore GitHub&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Explore GitHub;&quot;}" href="/explore">
      Explore GitHub
</a>  </li>

              <li class="color-fg-muted text-normal f6 text-mono mb-1 border-top pt-3 mt-3 mb-1">Learn and contribute</li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Topics&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Topics;&quot;}" href="/topics">
      Topics
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Collections&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Collections;&quot;}" href="/collections">
      Collections
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Trending&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Trending;&quot;}" href="/trending">
      Trending
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Skills&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Skills;&quot;}" href="https://skills.github.com/">
      Skills
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to GitHub Sponsors&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:GitHub Sponsors;&quot;}" href="/sponsors/explore">
      GitHub Sponsors
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Open source guides&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Open source guides;&quot;}" href="https://opensource.guide">
      Open source guides
</a>  </li>

              <li class="color-fg-muted text-normal f6 text-mono mb-1 border-top pt-3 mt-3 mb-1">Connect with others</li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to The ReadME Project&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:The ReadME Project;&quot;}" href="/readme">
      The ReadME Project
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Events&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Events;&quot;}" href="/events">
      Events
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to Community forum&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Community forum;&quot;}" href="https://github.community">
      Community forum
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to GitHub Education&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:GitHub Education;&quot;}" href="https://education.github.com">
      GitHub Education
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Explore&quot;,&quot;action&quot;:&quot;click to go to GitHub Stars program&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:GitHub Stars program;&quot;}" href="https://stars.github.com">
      GitHub Stars program
</a>  </li>

        </ul>
      </div>
    </details>
</li>


            <li class="mr-0 mr-lg-3 position-relative flex-wrap flex-justify-between flex-items-center border-bottom border-lg-bottom-0 d-block d-lg-flex flex-lg-nowrap flex-lg-items-center">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-analytics-event="{&quot;category&quot;:&quot;Header menu top item (logged out)&quot;,&quot;action&quot;:&quot;click to go to Marketplace&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Marketplace;&quot;}" href="/marketplace">Marketplace</a>
</li>


            <li class="mr-0 mr-lg-3 position-relative flex-wrap flex-justify-between flex-items-center border-bottom border-lg-bottom-0 d-block d-lg-flex flex-lg-nowrap flex-lg-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
      <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
        Pricing
        <svg x="0" y="0" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative"><path d="M1,1l6.2,6L13,1"></path></svg>
      </summary>
      <div class="dropdown-menu flex-auto rounded px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
        <ul class="list-style-none f5 pb-1">
              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--primary text-bold py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Pricing&quot;,&quot;action&quot;:&quot;click to go to Plans&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Plans;&quot;}" href="/pricing">
      Plans
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Pricing&quot;,&quot;action&quot;:&quot;click to go to Compare plans&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Compare plans;&quot;}" href="/pricing#compare-features">
      Compare plans
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--secondary py-2" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Pricing&quot;,&quot;action&quot;:&quot;click to go to Contact Sales&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Contact Sales;&quot;}" href="https://github.com/enterprise/contact">
      Contact Sales
</a>  </li>

              <li>
    <a class="lh-condensed-ultra d-block no-underline position-relative Link--primary text-bold border-top pt-4 pb-2 mt-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Pricing&quot;,&quot;action&quot;:&quot;click to go to Education&quot;,&quot;label&quot;:&quot;ref_page:/borisdayma/faceswap;ref_cta:Education;&quot;}" href="https://education.github.com">
      Education
</a>  </li>

        </ul>
      </div>
    </details>
</li>

          </ul>
        </nav>

      <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
          <div class="d-lg-flex min-width-0 mb-3 mb-lg-0">
            



<div class="header-search flex-auto js-site-search position-relative flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="211183970" data-scoped-search-url="/borisdayma/faceswap/search" data-owner-scoped-search-url="/users/borisdayma/search" data-unscoped-search-url="/search" data-turbo="false" action="/borisdayma/faceswap/search" accept-charset="UTF-8" method="get">
      <label class="form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey=s,/
          name="q"
          data-test-selector="nav-search-input"
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          role="combobox"
          aria-haspopup="listbox"
          aria-expanded="false"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
        >
        <input type="hidden" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" value="Sp3Of2YvPo4qxLeYR5mwenRVTlad6TdU866FD7O/z4RpEsvzq374WAFYaoy1Um787wvzEgvUi8MjNJYAeIY8Rg==" />
        <input type="hidden" class="js-site-search-type-field" name="type" >
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1 header-search-key-slash"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>


          <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
            
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="suggestion">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="color-fg-muted">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-owner-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="owner_scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this user">
        In this user
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="global_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

          </div>
      </label>
</form>  </div>
</div>

          </div>

        <div class="position-relative mr-3 mb-4 mb-lg-0 d-inline-block">
          <a href="/login?return_to=https%3A%2F%2Fgithub.com%2Fborisdayma%2Ffaceswap"
            class="HeaderMenu-link flex-shrink-0 no-underline"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="7999c50328689747bbd6bd41f632b1643860491bdd2bb57970d5620774702e1d"
            data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
            Sign in
          </a>
        </div>

          <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&amp;source=header-repo&amp;source_repo=borisdayma%2Ffaceswap"
            class="HeaderMenu-link flex-shrink-0 d-inline-block no-underline border color-border-default rounded px-2 py-1"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="7999c50328689747bbd6bd41f632b1643860491bdd2bb57970d5620774702e1d"
            data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;;ref_cta:Sign up;ref_loc:header logged out&quot;}"
          >
            Sign up
          </a>
      </div>
    </div>
  </div>
</header>

    </div>

  <div id="start-of-content" class="show-on-focus"></div>







    <div data-pjax-replace id="js-flash-container" data-turbo-replace>



  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div class="px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    
      <div>{{ message }}</div>

  </div>
</div>
  </template>
</div>


    
  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>





  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" data-pjax-container >
      
  




    






  <div id="repository-container-header" class="pt-3 hide-full-screen" style="background-color: var(--color-page-header-bg);" data-pjax-replace data-turbo-replace>

      <div class="d-flex flex-wrap flex-justify-end mb-3 px-3 px-md-4 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit mr-3">
            <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked color-fg-muted mr-2">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
  
  <span class="author flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/borisdayma/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/borisdayma">borisdayma</a>
  </span>
  <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap">faceswap</a>
  </strong>

  <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
</div>
  <span class="text-small lh-condensed-ultra no-wrap mt-1" data-repository-hovercards-enabled>
    forked from <a data-hovercard-type="repository" data-hovercard-url="/deepfakes/faceswap/hovercard" href="/deepfakes/faceswap">deepfakes/faceswap</a>
  </span>

        </div>

          <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

    

  <li>
        <a href="/login?return_to=%2Fborisdayma%2Ffaceswap" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="3543972464424ecab92ee1b4d90325d696e3cb417675d8a03a8058414c636b72" aria-label="You must be signed in to change notification settings" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path>
</svg>Notifications
</a>
  </li>

  <li>
      
    <a href="/login?return_to=%2Fborisdayma%2Ffaceswap" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:211183970,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="6d411d00339f04dc3fdee1eb2b4e39f64b8c235c65f415e4cafa4904cc0a3ce3" aria-label="You must be signed in to fork a repository" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" title="11,864" data-view-component="true" class="Counter">11.9k</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Fborisdayma%2Ffaceswap" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:211183970,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="13f73467008915e4aadef027f174b0bc827aa60c152de185058fd280a690661d" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="1 user starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-pjax-replace="true" data-turbo-replace="true" title="1" data-view-component="true" class="Counter js-social-count">1</span>
</a>        <button disabled="disabled" aria-label="You must be signed in to add this repository to a list" type="button" data-view-component="true" class="btn-sm btn BtnGroup-item px-2">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</button></div>
  </li>

  

</ul>

      </div>

      <div id="responsive-meta-container" data-pjax-replace data-turbo-replace>
      <div class="d-block d-md-none mb-2 px-3 px-md-4 px-lg-5">
      <p class="f4 mb-3">
        Deepfakes Software For All
      </p>
      <div class="mb-2 d-flex flex-items-center">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link flex-shrink-0 mr-2">
    <path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path>
</svg>
        <span class="flex-auto min-width-0 css-truncate css-truncate-target width-fit">
          <a title="https://www.faceswap.dev" role="link" target="_blank" class="text-bold" rel="noopener noreferrer" href="https://www.faceswap.dev">www.faceswap.dev</a>
        </span>
      </div>

    <h3 class="sr-only">License</h3>
  <div class="mb-2">
    <a href="/borisdayma/faceswap/blob/master/LICENSE"
      class="Link--muted"
      
      data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:license&quot;}"
    >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-2">
    <path fill-rule="evenodd" d="M8.75.75a.75.75 0 00-1.5 0V2h-.984c-.305 0-.604.08-.869.23l-1.288.737A.25.25 0 013.984 3H1.75a.75.75 0 000 1.5h.428L.066 9.192a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.514 3.514 0 00.686.45A4.492 4.492 0 003 11c.88 0 1.556-.22 2.023-.454a3.515 3.515 0 00.686-.45l.045-.04.016-.015.006-.006.002-.002.001-.002L5.25 9.5l.53.53a.75.75 0 00.154-.838L3.822 4.5h.162c.305 0 .604-.08.869-.23l1.289-.737a.25.25 0 01.124-.033h.984V13h-2.5a.75.75 0 000 1.5h6.5a.75.75 0 000-1.5h-2.5V3.5h.984a.25.25 0 01.124.033l1.29.736c.264.152.563.231.868.231h.162l-2.112 4.692a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.517 3.517 0 00.686.45A4.492 4.492 0 0013 11c.88 0 1.556-.22 2.023-.454a3.512 3.512 0 00.686-.45l.045-.04.01-.01.006-.005.006-.006.002-.002.001-.002-.529-.531.53.53a.75.75 0 00.154-.838L13.823 4.5h.427a.75.75 0 000-1.5h-2.234a.25.25 0 01-.124-.033l-1.29-.736A1.75 1.75 0 009.735 2H8.75V.75zM1.695 9.227c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327l-1.305 2.9zm10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327l-1.305 2.9z"></path>
</svg>
     GPL-3.0 license
    </a>
  </div>


    <div class="mb-3">
      <a class="Link--secondary no-underline mr-3" href="/borisdayma/faceswap/stargazers">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
        <span class="text-bold">1</span>
        star
</a>      <a class="Link--secondary no-underline" href="/borisdayma/faceswap/network/members">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-1">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
        <span class="text-bold">11.9k</span>
        forks
</a>    </div>
    <div class="d-flex">
      <div class="flex-1 mr-2">
          <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Fborisdayma%2Ffaceswap" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:211183970,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="13f73467008915e4aadef027f174b0bc827aa60c152de185058fd280a690661d" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn btn-block BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>
</a>        <button disabled="disabled" aria-label="You must be signed in to add this repository to a list" type="button" data-view-component="true" class="btn-sm btn BtnGroup-item px-2">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</button></div>
      </div>
      <div class="flex-1">
            <a href="/login?return_to=%2Fborisdayma%2Ffaceswap" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="3543972464424ecab92ee1b4d90325d696e3cb417675d8a03a8058414c636b72" aria-label="You must be signed in to change notification settings" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn btn-block">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path>
</svg>Notifications
</a>
      </div>
    </div>
  </div>

</div>


        

  
<nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/borisdayma/faceswap" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /borisdayma/faceswap" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/borisdayma/faceswap/pulls" data-tab-item="i1pull-requests-tab" data-selected-links="repo_pulls checks /borisdayma/faceswap/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/borisdayma/faceswap/actions" data-tab-item="i2actions-tab" data-selected-links="repo_actions /borisdayma/faceswap/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Actions&quot;,&quot;action&quot;:&quot;clicked&quot;,&quot;label&quot;:&quot;ref_cta:Actions;ref_loc:navigation_helper&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/borisdayma/faceswap/projects?type=new" data-tab-item="i3projects-tab" data-selected-links="repo_projects new_repo_project repo_project /borisdayma/faceswap/projects?type=new" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0114.25 16H1.75A1.75 1.75 0 010 14.25V1.75zM1.5 6.5v7.75c0 .138.112.25.25.25H5v-8H1.5zM5 5H1.5V1.75a.25.25 0 01.25-.25H5V5zm1.5 1.5v8h7.75a.25.25 0 00.25-.25V6.5h-8zm8-1.5h-8V1.5h7.75a.25.25 0 01.25.25V5z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="wiki-tab" href="/borisdayma/faceswap/wiki" data-tab-item="i4wiki-tab" data-selected-links="repo_wiki /borisdayma/faceswap/wiki" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g w" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path>
</svg>
        <span data-content="Wiki">Wiki</span>
          <span id="wiki-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/borisdayma/faceswap/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /borisdayma/faceswap/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/borisdayma/faceswap/security/overall-count" accept="text/fragment+html"></include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/borisdayma/faceswap/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /borisdayma/faceswap/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <details data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
  <div data-view-component="true">          <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
  
            <ul>
                <li data-menu-item="i0code-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item selected dropdown-item" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /borisdayma/faceswap" href="/borisdayma/faceswap">
                    Code
</a>                </li>
                <li data-menu-item="i1pull-requests-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /borisdayma/faceswap/pulls" href="/borisdayma/faceswap/pulls">
                    Pull requests
</a>                </li>
                <li data-menu-item="i2actions-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /borisdayma/faceswap/actions" href="/borisdayma/faceswap/actions">
                    Actions
</a>                </li>
                <li data-menu-item="i3projects-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /borisdayma/faceswap/projects?type=new" href="/borisdayma/faceswap/projects?type=new">
                    Projects
</a>                </li>
                <li data-menu-item="i4wiki-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_wiki /borisdayma/faceswap/wiki" href="/borisdayma/faceswap/wiki">
                    Wiki
</a>                </li>
                <li data-menu-item="i5security-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /borisdayma/faceswap/security" href="/borisdayma/faceswap/security">
                    Security
</a>                </li>
                <li data-menu-item="i6insights-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /borisdayma/faceswap/pulse" href="/borisdayma/faceswap/pulse">
                    Insights
</a>                </li>
            </ul>

</details-menu></div>
</details></div>
</nav>

  </div>




  <turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
      <div id="repo-content-pjax-container" class="repository-content " >
    
    


    
      
  <h1 class='sr-only'>borisdayma/faceswap</h1>
  <div class="clearfix container-xl px-3 px-md-4 px-lg-5 mt-4">
    

<div>
  

  <div class="d-none d-lg-block mt-6 mr-3 Popover top-0 right-0 color-shadow-medium col-3">
    
  </div>

  <div id="spoof-warning" class="mt-0 pb-3" hidden aria-hidden>
  <div data-view-component="true" class="flash flash-warn mt-0 clearfix">
  
  
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert float-left mt-1">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>

      <div class="overflow-hidden">This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.</div>


  
</div></div>

  <include-fragment src="/borisdayma/faceswap/spoofed_commit_check/46efae3506ffd31900a70887b75b5a795f02d52d" data-test-selector="spoofed-commit-check"></include-fragment>

  <div data-view-component="true" class="Layout Layout--flowRow-until-md Layout--sidebarPosition-end Layout--sidebarPosition-flowRow-end">
  <div data-view-component="true" class="Layout-main">      
      
      <div class="file-navigation mb-3 d-flex flex-items-start">
  
<div class="position-relative">
  <details class="details-reset details-overlay mr-0 mb-0 " id="branch-select-menu">
    <summary class="btn css-truncate"
            data-hotkey="w"
            title="Switch branches or tags">
      <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
      <span class="css-truncate-target" data-menu-button>master</span>
      <span class="dropdown-caret"></span>
    </summary>

    
<div class="SelectMenu">
  <div class="SelectMenu-modal">
    <header class="SelectMenu-header">
      <span class="SelectMenu-title">Switch branches/tags</span>
      <button class="SelectMenu-closeButton" type="button" data-toggle-for="branch-select-menu"><svg aria-label="Close menu" aria-hidden="false" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg></button>
    </header>

    <input-demux data-action="tab-container-change:input-demux#storeInput tab-container-changed:input-demux#updateInput">
      <tab-container class="d-flex flex-column js-branches-tags-tabs" style="min-height: 0;">
        <div class="SelectMenu-filter">
          <input data-target="input-demux.source"
                 id="context-commitish-filter-field"
                 class="SelectMenu-input form-control"
                 aria-owns="ref-list-branches"
                 data-controls-ref-menu-id="ref-list-branches"
                 autofocus
                 autocomplete="off"
                 aria-label="Filter branches/tags"
                 placeholder="Filter branches/tags"
                 type="text"
          >
        </div>

        <div class="SelectMenu-tabs" role="tablist" data-target="input-demux.control" >
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="true">Branches</button>
          <button class="SelectMenu-tab" type="button" role="tab">Tags</button>
        </div>

        <div role="tabpanel" id="ref-list-branches" data-filter-placeholder="Filter branches/tags" tabindex="" class="d-flex flex-column flex-auto overflow-auto">
          <ref-selector
            type="branch"
            data-targets="input-demux.sinks"
            data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            "
            query-endpoint="/borisdayma/faceswap/refs"
            
            cache-key="v0:1569600744.0"
            current-committish="bWFzdGVy"
            default-branch="bWFzdGVy"
            name-with-owner="Ym9yaXNkYXltYS9mYWNlc3dhcA=="
            prefetch-on-mouseover
          >

            <template data-target="ref-selector.fetchFailedTemplate">
              <div class="SelectMenu-message" data-index="{{ index }}">Could not load branches</div>
            </template>

              <template data-target="ref-selector.noMatchTemplate">
    <div class="SelectMenu-message">Nothing to show</div>
</template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list " data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
              <div class="SelectMenu-loading pt-3 pb-0 overflow-hidden" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
              </div>
            </div>

              <template data-target="ref-selector.itemTemplate">
  <a href="https://github.com/borisdayma/faceswap/tree/{{ urlEncodedRefName }}" class="SelectMenu-item" role="menuitemradio" rel="nofollow" aria-checked="{{ isCurrent }}" data-index="{{ index }}">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    <span class="flex-1 css-truncate css-truncate-overflow {{ isFilteringClass }}">{{ refName }}</span>
    <span hidden="{{ isNotDefault }}" class="Label Label--secondary flex-self-start">default</span>
  </a>
</template>


              <footer class="SelectMenu-footer"><a href="/borisdayma/faceswap/branches">View all branches</a></footer>
          </ref-selector>

        </div>

        <div role="tabpanel" id="tags-menu" data-filter-placeholder="Find a tag" tabindex="" hidden class="d-flex flex-column flex-auto overflow-auto">
          <ref-selector
            type="tag"
            data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            "
            data-targets="input-demux.sinks"
            query-endpoint="/borisdayma/faceswap/refs"
            cache-key="v0:1569600744.0"
            current-committish="bWFzdGVy"
            default-branch="bWFzdGVy"
            name-with-owner="Ym9yaXNkYXltYS9mYWNlc3dhcA=="
          >

            <template data-target="ref-selector.fetchFailedTemplate">
              <div class="SelectMenu-message" data-index="{{ index }}">Could not load tags</div>
            </template>

            <template data-target="ref-selector.noMatchTemplate">
              <div class="SelectMenu-message" data-index="{{ index }}">Nothing to show</div>
            </template>

              <template data-target="ref-selector.itemTemplate">
  <a href="https://github.com/borisdayma/faceswap/tree/{{ urlEncodedRefName }}" class="SelectMenu-item" role="menuitemradio" rel="nofollow" aria-checked="{{ isCurrent }}" data-index="{{ index }}">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    <span class="flex-1 css-truncate css-truncate-overflow {{ isFilteringClass }}">{{ refName }}</span>
    <span hidden="{{ isNotDefault }}" class="Label Label--secondary flex-self-start">default</span>
  </a>
</template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
              <div class="SelectMenu-loading pt-3 pb-0 overflow-hidden" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
              </div>
            </div>
              <footer class="SelectMenu-footer"><a href="/borisdayma/faceswap/tags">View all tags</a></footer>
          </ref-selector>
        </div>
      </tab-container>
    </input-demux>
  </div>
</div>

  </details>

</div>


  <div class="flex-self-center ml-3 flex-self-stretch d-none d-lg-flex flex-items-center lh-condensed-ultra">
    <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/branches" class="Link--primary no-underline">
          <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
          <strong>6</strong>
          <span class="color-fg-muted">branches</span>
    </a>
    <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tags" class="ml-3 Link--primary no-underline">
      <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag">
    <path fill-rule="evenodd" d="M2.5 7.775V2.75a.25.25 0 01.25-.25h5.025a.25.25 0 01.177.073l6.25 6.25a.25.25 0 010 .354l-5.025 5.025a.25.25 0 01-.354 0l-6.25-6.25a.25.25 0 01-.073-.177zm-1.5 0V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 010 2.474l-5.026 5.026a1.75 1.75 0 01-2.474 0l-6.25-6.25A1.75 1.75 0 011 7.775zM6 5a1 1 0 100 2 1 1 0 000-2z"></path>
</svg>
        <strong>2</strong>
        <span class="color-fg-muted">tags</span>
    </a>
  </div>

  <div class="flex-auto"></div>

  <include-fragment data-test-selector="overview-actions-fragment" src="/borisdayma/faceswap/overview_actions/master"></include-fragment>


    <span class="d-none d-md-flex ml-2">
      
<get-repo class="">
    
    <details class="position-relative details-overlay details-reset js-codespaces-details-container"
             data-action="toggle:get-repo#onDetailsToggle"
             
    >
        <summary data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:211183970,&quot;target&quot;:&quot;CLONE_OR_DOWNLOAD_BUTTON&quot;,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="7ecff16bf15eeaf550ef81f97020e0516fa901eca2f9b6c6a8d53c31d70b0e99" data-view-component="true" class="btn-primary btn">    Code<span class="dropdown-caret"></span>
</summary>      <div class="position-relative">
        <div class="dropdown-menu dropdown-menu-sw p-0" style="top:6px;width:378px;">
          <div
  data-target="get-repo.modal"
  
>
    <ul class="list-style-none">
        <li class="Box-row p-3">
  <a class="Link--muted float-right tooltipped tooltipped-s" href="https://docs.github.com/articles/which-remote-url-should-i-use" target="_blank" aria-label="Which remote URL should I use?">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-question">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path>
</svg>
</a>

<div class="text-bold">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-terminal mr-2">
    <path fill-rule="evenodd" d="M0 2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0114.25 15H1.75A1.75 1.75 0 010 13.25V2.75zm1.75-.25a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V2.75a.25.25 0 00-.25-.25H1.75zM7.25 8a.75.75 0 01-.22.53l-2.25 2.25a.75.75 0 11-1.06-1.06L5.44 8 3.72 6.28a.75.75 0 111.06-1.06l2.25 2.25c.141.14.22.331.22.53zm1.5 1.5a.75.75 0 000 1.5h3a.75.75 0 000-1.5h-3z"></path>
</svg>
  Clone
</div>

<tab-container>

  <div class="UnderlineNav my-2 box-shadow-none">
    <div class="UnderlineNav-body" role="tablist">
          <button name="button" type="button" role="tab" class="UnderlineNav-item" aria-selected="true" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_HTTPS&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="cbd0dc9d31bc5c386cd781516591d654a643f72c168b4174bdeaa3cce3d5f4ad">
            HTTPS
</button>          <button name="button" type="button" role="tab" class="UnderlineNav-item" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_GH_CLI&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="d44749537f2cd8a34d949736515e8e932e4c548732b18e03ea461874c51dc4c6">
            GitHub CLI
</button>    </div>
  </div>

  <div role="tabpanel">
    <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm color-bg-subtle" data-autoselect value="https://github.com/borisdayma/faceswap.git" aria-label="https://github.com/borisdayma/faceswap.git" readonly>
  <div class="input-group-button">
    <clipboard-copy value="https://github.com/borisdayma/faceswap.git" aria-label="Copy to clipboard" class="btn btn-sm js-clipboard-copy tooltipped-no-delay ClipboardButton js-clone-url-http" data-copy-feedback="Copied!" data-tooltip-direction="n" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="77b67437295ab51ea7f76ed65cd48a3df305b1e87585fdc3ab8f84df0531b32b"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon d-inline-block">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-inline-block d-sm-none">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg></clipboard-copy>
  </div>
</div>

    <p class="mt-2 mb-0 f6 color-fg-muted">
        Use Git or checkout with SVN using the web URL.
    </p>
  </div>


  <div role="tabpanel" hidden>
    <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm color-bg-subtle" data-autoselect value="gh repo clone borisdayma/faceswap" aria-label="gh repo clone borisdayma/faceswap" readonly>
  <div class="input-group-button">
    <clipboard-copy value="gh repo clone borisdayma/faceswap" aria-label="Copy to clipboard" class="btn btn-sm js-clipboard-copy tooltipped-no-delay ClipboardButton js-clone-url-gh-cli" data-copy-feedback="Copied!" data-tooltip-direction="n" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="77b67437295ab51ea7f76ed65cd48a3df305b1e87585fdc3ab8f84df0531b32b"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon d-inline-block">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-inline-block d-sm-none">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg></clipboard-copy>
  </div>
</div>

    <p class="mt-2 mb-0 f6 color-fg-muted">
      Work fast with our official CLI.
      <a href="https://cli.github.com" target="_blank">Learn more</a>.
    </p>
  </div>
</tab-container>

</li>
<li data-platforms="windows,mac" class="Box-row Box-row--hover-gray p-3 mt-0 rounded-0 js-remove-unless-platform">
  <a class="d-flex flex-items-center color-fg-default text-bold no-underline" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;OPEN_IN_DESKTOP&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="d909725575f411ebcb95acd62ececfbf0aa8daf9baa3ebdd0375d2a94d36bd72" data-action="click:get-repo#showDownloadMessage" href="https://desktop.github.com">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-desktop-download mr-2">
    <path d="M4.927 5.427l2.896 2.896a.25.25 0 00.354 0l2.896-2.896A.25.25 0 0010.896 5H8.75V.75a.75.75 0 10-1.5 0V5H5.104a.25.25 0 00-.177.427z"></path><path d="M1.573 2.573a.25.25 0 00-.073.177v7.5a.25.25 0 00.25.25h12.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-3a.75.75 0 110-1.5h3A1.75 1.75 0 0116 2.75v7.5A1.75 1.75 0 0114.25 12h-3.727c.099 1.041.52 1.872 1.292 2.757A.75.75 0 0111.25 16h-6.5a.75.75 0 01-.565-1.243c.772-.885 1.192-1.716 1.292-2.757H1.75A1.75 1.75 0 010 10.25v-7.5A1.75 1.75 0 011.75 1h3a.75.75 0 010 1.5h-3a.25.25 0 00-.177.073zM6.982 12a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5H6.982z"></path>
</svg>
    Open with GitHub Desktop
</a></li>
<li class="Box-row Box-row--hover-gray p-3 mt-0" >
  <a class="d-flex flex-items-center color-fg-default text-bold no-underline" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;DOWNLOAD_ZIP&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="46489ccfafdf88afb6ef15a44a14f0edd8c63d7c95d4026071268fd1c08526f8" data-ga-click="Repository, download zip, location:repo overview" data-open-app="link" href="/borisdayma/faceswap/archive/refs/heads/master.zip">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-zip mr-2">
    <path fill-rule="evenodd" d="M3.5 1.75a.25.25 0 01.25-.25h3a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h2.086a.25.25 0 01.177.073l2.914 2.914a.25.25 0 01.073.177v8.586a.25.25 0 01-.25.25h-.5a.75.75 0 000 1.5h.5A1.75 1.75 0 0014 13.25V4.664c0-.464-.184-.909-.513-1.237L10.573.513A1.75 1.75 0 009.336 0H3.75A1.75 1.75 0 002 1.75v11.5c0 .649.353 1.214.874 1.515a.75.75 0 10.752-1.298.25.25 0 01-.126-.217V1.75zM8.75 3a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5zM6 5.25a.75.75 0 01.75-.75h.5a.75.75 0 010 1.5h-.5A.75.75 0 016 5.25zm2 1.5A.75.75 0 018.75 6h.5a.75.75 0 010 1.5h-.5A.75.75 0 018 6.75zm-1.25.75a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5zM8 9.75A.75.75 0 018.75 9h.5a.75.75 0 010 1.5h-.5A.75.75 0 018 9.75zm-.75.75a1.75 1.75 0 00-1.75 1.75v3c0 .414.336.75.75.75h2.5a.75.75 0 00.75-.75v-3a1.75 1.75 0 00-1.75-1.75h-.5zM7 12.25a.25.25 0 01.25-.25h.5a.25.25 0 01.25.25v2.25H7v-2.25z"></path>
</svg>
    Download ZIP
</a></li>

    </ul>
</div>


<div class="p-3" data-targets="get-repo.platforms" data-platform="mac" hidden>
  <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="AnimatedEllipsis"></span></h4>
  <p class="color-fg-muted">
    If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.
  </p>
    <button data-action="click:get-repo#onDetailsToggle" type="button" data-view-component="true" class="btn-link">
</button>
</div>
<div class="p-3" data-targets="get-repo.platforms" data-platform="windows" hidden>
  <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="AnimatedEllipsis"></span></h4>
  <p class="color-fg-muted">
    If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.
  </p>
    <button data-action="click:get-repo#onDetailsToggle" type="button" data-view-component="true" class="btn-link">
</button>
</div>
<div class="p-3" data-targets="get-repo.platforms" data-platform="xcode" hidden>
  <h4 class="lh-condensed mb-3">Launching Xcode<span class="AnimatedEllipsis"></span></h4>
  <p class="color-fg-muted">
    If nothing happens, <a href="https://developer.apple.com/xcode/">download Xcode</a> and try again.
  </p>
    <button data-action="click:get-repo#onDetailsToggle" type="button" data-view-component="true" class="btn-link">
</button>
</div>
<div class="p-3 " data-targets="get-repo.platforms" data-target="new-codespace.loadingVscode create-button.loadingVscode" data-platform="vscode" hidden>
  <poll-include-fragment data-target="get-repo.vscodePoller new-codespace.vscodePoller create-button.vscodePoller">
    <h4 class="lh-condensed mb-3">Launching Visual Studio Code<span class="AnimatedEllipsis" data-hide-on-error></span></h4>
    <p class="color-fg-muted" data-hide-on-error>Your codespace will open once ready.</p>
    <p class="color-fg-muted" data-show-on-error hidden>There was a problem preparing your codespace, please try again.</p>
  </poll-include-fragment>
</div>


        </div>
      </div>
    </details>

</get-repo>

        
    </span>
</div>



      

<div class="d-sm-flex Box mb-3 Box-body color-bg-subtle">
  <div class="d-flex flex-auto">
        <div>
          This branch is <span><a data-analytics-event="{&quot;category&quot;:&quot;Branch Infobar&quot;,&quot;action&quot;:&quot;Behind Compare&quot;,&quot;label&quot;:&quot;ref_loc:bar;is_fork:true&quot;}" href="/borisdayma/faceswap/compare/master...deepfakes:faceswap:master">689 commits behind</a> deepfakes:master</span>.
        </div>
  </div>
  <div class="d-flex flex-justify-end mt-2 mt-sm-0 ml-sm-3">
      <details class="details-overlay details-reset position-relative">
        <summary
          class="btn-link no-underline color-fg-muted"
          aria-haspopup="menu"
          role="button"
          data-analytics-event="{&quot;category&quot;:&quot;Branch Infobar&quot;,&quot;action&quot;:&quot;Open Contribute dropdown&quot;,&quot;label&quot;:&quot;ref_loc:contribute_dropdown;is_fork:true&quot;}"
        >
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path>
</svg>
          Contribute
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
        </summary>
        <div class="position-relative">
          <div class="dropdown-menu dropdown-menu-sw pb-0 branch-contribute-right branch-info-dropdown-size">
            <ul class="list-style-none">
              <li class="d-flex p-3">
                <div class="mr-2">
                  <div class="completeness-indicator completeness-indicator-problem">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path>
</svg>
                  </div>
                </div>
                <div>
                  <p class="text-bold mb-1">
                      This branch is not ahead of the upstream deepfakes:master.
                  </p>
                  <p class="text-small color-fg-muted mb-0">
                      No new commits yet. Enjoy your day!
                  </p>
                </div>
              </li>
              <li class="Box-row Box-row--gray p-3">
                <div class="d-flex">

                  <a href="/borisdayma/faceswap/compare/deepfakes:faceswap:master...master?expand=1"
                    class="btn btn-primary btn-block flex-1 disabled"
                    data-analytics-event="{&quot;category&quot;:&quot;Branch Infobar&quot;,&quot;action&quot;:&quot;Open pull request&quot;,&quot;label&quot;:&quot;ref_loc:contribute_dropdown;is_fork:true&quot;}"
                  >
                    Open pull request
                  </a>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </details>
  </div>
</div>


<div class="Box mb-3">
  <div class="Box-header position-relative">
    <h2 class="sr-only">Latest commit</h2>
    <div class="js-details-container Details d-flex rounded-top-2 flex-items-center flex-wrap" data-issue-and-pr-hovercards-enabled>
      
  <div class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1 hx_avatar_stack_commit" >
    
<div class="AvatarStack flex-self-start  " >
  <div class="AvatarStack-body" aria-label="torzdf" >
      <a class="avatar avatar-user" style="width:24px;height:24px;" data-skip-pjax="true" data-test-selector="commits-avatar-stack-avatar-link" data-hovercard-type="user" data-hovercard-url="/users/torzdf/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/torzdf">
        <img data-test-selector="commits-avatar-stack-avatar-image" src="https://avatars.githubusercontent.com/u/36920800?s=48&amp;v=4" width="24" height="24" alt="@torzdf" class=" avatar-user" />
</a>  </div>
</div>

  </div>
  <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
    <div class="css-truncate css-truncate-overflow color-fg-muted" >
          <a class="commit-author user-mention" title="View all commits by torzdf" href="/borisdayma/faceswap/commits?author=torzdf">torzdf</a>
    
  

        <span class="d-none d-sm-inline">
          <a data-pjax="true" data-test-selector="commit-tease-commit-message" title="Alignments tool: Remove extract-large and add `large` option" class="Link--primary markdown-title" href="/borisdayma/faceswap/commit/46efae3506ffd31900a70887b75b5a795f02d52d">Alignments tool: Remove extract-large and add <code>large</code> option</a>
        </span>
    </div>
    <span
      class="hidden-text-expander ml-2 d-inline-block d-inline-block d-lg-none"
      
    >
      <button
        type="button"
        class="color-fg-default ellipsis-expander js-details-target"
        aria-expanded="false"
        
      >
        &hellip;
      </button>
    </span>
    <div class="d-flex flex-auto flex-justify-end ml-3 flex-items-baseline">
        <include-fragment accept="text/fragment+html" src="/borisdayma/faceswap/commit/46efae3506ffd31900a70887b75b5a795f02d52d/rollup?direction=sw" class="d-inline" ></include-fragment>
      <a
        href="/borisdayma/faceswap/commit/46efae3506ffd31900a70887b75b5a795f02d52d"
        class="f6 Link--secondary text-mono ml-2 d-none d-lg-inline"
        data-pjax="#repo-content-pjax-container"
        data-turbo-frame="repo-content-turbo-frame"
        
      >
        46efae3
      </a>
      <a
        href="/borisdayma/faceswap/commit/46efae3506ffd31900a70887b75b5a795f02d52d"
        class="Link--secondary ml-2"
        data-pjax="#repo-content-pjax-container"
        data-turbo-frame="repo-content-turbo-frame"
        
      >
        <relative-time datetime="2019-09-26T17:22:22Z" class="no-wrap">Sep 26, 2019</relative-time>
      </a>
    </div>
  </div>
  <div class="pl-0 pl-md-5 flex-order-1 width-full Details-content--hidden">
      <div class="mt-2">
        <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-test-selector="commit-tease-commit-message" class="Link--primary text-bold" href="/borisdayma/faceswap/commit/46efae3506ffd31900a70887b75b5a795f02d52d">Alignments tool: Remove extract-large and add `large` option</a>
      </div>
    <div class="d-flex flex-items-center">
      <code class="border d-lg-none mt-2 px-1 rounded-2">46efae3</code>
    </div>
  </div>
      <div class="flex-shrink-0">
        <h2 class="sr-only">Git stats</h2>
        <ul class="list-style-none d-flex">
          <li class="ml-0 ml-md-3">
            <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/commits/master" class="pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap">
              <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path>
</svg>
              <span class="d-none d-sm-inline">
                    <strong>898</strong>
                    <span aria-label="Commits on master" class="color-fg-muted d-none d-lg-inline">
                      commits
                    </span>
              </span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
    <h2 id="files"  class="sr-only">Files</h2>
    


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/borisdayma/faceswap/tree/46efae3506ffd31900a70887b75b5a795f02d52d">Permalink</a>

  <div data-view-component="true" class="include-fragment-error flash flash-error flash-full py-2">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
  
    Failed to load latest commit information.


  
</div>  <div class="js-details-container Details" data-hpc>
    <div role="grid" aria-labelledby="files" class="Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block" data-pjax>
      <div class="sr-only" role="row">
        <div role="columnheader">Type</div>
        <div role="columnheader">Name</div>
        <div role="columnheader" class="d-none d-md-block">Latest commit message</div>
        <div role="columnheader">Commit time</div>
      </div>

        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title=".github" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/.github">.github</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Update ISSUE_TEMPLATE.md" class="Link--secondary" href="/borisdayma/faceswap/commit/48bd90326d56e6835fdfb5ee4fc5e6b2a37dfd09">Update ISSUE_TEMPLATE.md</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-25T10:03:01Z" data-view-component="true" class="no-wrap">Sep 25, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="This path skips through empty directories" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/.install/windows"><span class="color-fg-muted">.install/</span>windows</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Installer: Pop faceswap.dev on installer completion" class="Link--secondary" href="/borisdayma/faceswap/commit/ba5130796cad878a80f66def0f73d0b7d80ff42b">Installer: Pop faceswap.dev on installer completion</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-07-31T22:33:43Z" data-view-component="true" class="no-wrap">Jul 31, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="_travis" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/_travis">_travis</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Moved travis test to _travis + wmv support" class="Link--secondary" href="/borisdayma/faceswap/commit/e2609c18442e4a97636fdf0ebde04783883a1a55">Moved travis test to _travis + wmv support</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-22T18:00:42Z" data-view-component="true" class="no-wrap">Sep 22, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="config" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/config">config</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="model_refactor (#571) (#572)

* model_refactor (#571)

* original model to new structure

* IAE model to new structure

* OriginalHiRes to new structure

* Fix trainer for different resolutions

* Initial config implementation

* Configparse library added

* improved training data loader

* dfaker model working

* Add logging to training functions

* Non blocking input for cli training

* Add error handling to threads. Add non-mp queues to queue_handler

* Improved Model Building and NNMeta

* refactor lib/models

* training refactor. DFL H128 model Implementation

* Dfaker - use hashes

* Move timelapse. Remove perceptual loss arg

* Update INSTALL.md. Add logger formatting. Update Dfaker training

* DFL h128 partially ported

* Add mask to dfaker (#573)

* Remove old models. Add mask to dfaker

* dfl mask. Make masks selectable in config (#575)

* DFL H128 Mask. Mask type selectable in config.

* remove gan_v2_2

* Creating Input Size config for models

Creating Input Size config for models

Will be used downstream in converters.

Also name change of image_shape to input_shape to clarify ( for future models with potentially different output_shapes)

* Add mask loss options to config

* MTCNN options to config.ini. Remove GAN config. Update USAGE.md

* Add sliders for numerical values in GUI

* Add config plugins menu to gui. Validate config

* Only backup model if loss has dropped. Get training working again

* bugfixes

* Standardise loss printing

* GUI idle cpu fixes. Graph loss fix.

* mutli-gpu logging bugfix

* Merge branch 'staging' into train_refactor

* backup state file

* Crash protection: Only backup if both total losses have dropped

* Port OriginalHiRes_RC4 to train_refactor (OriginalHiRes)

* Load and save model structure with weights

* Slight code update

* Improve config loader. Add subpixel opt to all models. Config to state

* Show samples... wrong input

* Remove AE topology. Add input/output shapes to State

* Port original_villain (birb/VillainGuy) model to faceswap

* Add plugin info to GUI config pages

* Load input shape from state. IAE Config options.

* Fix transform_kwargs.
Coverage to ratio.
Bugfix mask detection

* Suppress keras userwarnings.
Automate zoom.
Coverage_ratio to model def.

* Consolidation of converters &amp; refactor (#574)

* Consolidation of converters &amp; refactor

Initial Upload of alpha

Items
- consolidate convert_mased &amp; convert_adjust into one converter
-add average color adjust to convert_masked
-allow mask transition blur size to be a fixed integer of pixels and a fraction of the facial mask size
-allow erosion/dilation size to be a fixed integer of pixels and a fraction of the facial mask size
-eliminate redundant type conversions to avoid multiple round-off errors
-refactor loops for vectorization/speed
-reorganize for clarity &amp; style changes

TODO
- bug/issues with warping the new face onto a transparent old image...use a cleanup mask for now
- issues with mask border giving black ring at zero erosion .. investigate
- remove GAN ??
- test enlargment factors of umeyama standard face .. match to coverage factor
- make enlargment factor a model parameter
- remove convert_adjusted and referencing code when finished

* Update Convert_Masked.py

default blur size of 2 to match original...
description of enlargement tests
breakout matrxi scaling into def

* Enlargment scale as a cli parameter

* Update cli.py

* dynamic interpolation algorithm

Compute x &amp; y scale factors from the affine matrix on the fly by QR decomp.
Choose interpolation alogrithm for the affine warp based on an upsample or downsample for each image

* input size
input size from config

* fix issues with &lt;1.0 erosion

* Update convert.py

* Update Convert_Adjust.py

more work on the way to merginf

* Clean up help note on sharpen

* cleanup seamless

* Delete Convert_Adjust.py

* Update umeyama.py

* Update training_data.py

* swapping

* segmentation stub

* changes to convert.str

* Update masked.py

* Backwards compatibility fix for models
Get converter running

* Convert:
Move masks to class.
bugfix blur_size
some linting

* mask fix

* convert fixes

- missing facehull_rect re-added
- coverage to %
- corrected coverage logic
- cleanup of gui option ordering

* Update cli.py

* default for blur

* Update masked.py

* added preliminary low_mem version of OriginalHighRes model plugin

* Code cleanup, minor fixes

* Update masked.py

* Update masked.py

* Add dfl mask to convert

* histogram fix &amp; seamless location

* update

* revert

* bugfix: Load actual configuration in gui

* Standardize nn_blocks

* Update cli.py

* Minor code amends

* Fix Original HiRes model

* Add masks to preview output for mask trainers
refactor trainer.__base.py

* Masked trainers converter support

* convert bugfix

* Bugfix: Converter for masked (dfl/dfaker) trainers

* Additional Losses (#592)

* initial upload

* Delete blur.py

* default initializer = He instead of Glorot (#588)

* Allow kernel_initializer to be overridable

* Add ICNR Initializer option for upscale on all models.

* Hopefully fixes RSoDs with original-highres model plugin

* remove debug line

* Original-HighRes model plugin Red Screen of Death fix, take #2

* Move global options to _base. Rename Villain model

* clipnorm and res block biases

* scale the end of res block

* res block

* dfaker pre-activation res

* OHRES pre-activation

* villain pre-activation

* tabs/space in nn_blocks

* fix for histogram with mask all set to zero

* fix to prevent two networks with same name

* GUI: Wider tooltips. Improve TQDM capture

* Fix regex bug

* Convert padding=48 to ratio of image size

* Add size option to alignments tool extract

* Pass through training image size to convert from model

* Convert: Pull training coverage from model

* convert: coverage, blur and erode to percent

* simplify matrix scaling

* ordering of sliders in train

* Add matrix scaling to utils. Use interpolation in lib.aligner transform

* masked.py Import get_matrix_scaling from utils

* fix circular import

* Update masked.py

* quick fix for matrix scaling

* testing thus for now

* tqdm regex capture bugfix

* Minor ammends

* blur size cleanup

* Remove coverage option from convert (Now cascades from model)

* Implement convert for all model types

* Add mask option and coverage option to all existing models

* bugfix for model loading on convert

* debug print removal

* Bugfix for masks in dfl_h128 and iae

* Update preview display. Add preview scaling to cli

* mask notes

* Delete training_data_v2.py

errant file

* training data variables

* Fix timelapse function

* Add new config items to state file for legacy purposes

* Slight GUI tweak

* Raise exception if problem with loaded model

* Add Tensorboard support (Logs stored in model directory)

* ICNR fix

* loss bugfix

* convert bugfix

* Move ini files to config folder. Make TensorBoard optional

* Fix training data for unbalanced inputs/outputs

* Fix config &quot;none&quot; test

* Keep helptext in .ini files when saving config from GUI

* Remove frame_dims from alignments

* Add no-flip and warp-to-landmarks cli options

* Revert OHR to RC4_fix version

* Fix lowmem mode on OHR model

* padding to variable

* Save models in parallel threads

* Speed-up of res_block stability

* Automated Reflection Padding

* Reflect Padding as a training option

Includes auto-calculation of proper padding shapes, input_shapes, output_shapes

Flag included in config now

* rest of reflect padding

* Move TB logging to cli. Session info to state file

* Add session iterations to state file

* Add recent files to menu. GUI code tidy up

* [GUI] Fix recent file list update issue

* Add correct loss names to TensorBoard logs

* Update live graph to use TensorBoard and remove animation

* Fix analysis tab. GUI optimizations

* Analysis Graph popup to Tensorboard Logs

* [GUI] Bug fix for graphing for models with hypens in name

* [GUI] Correctly split loss to tabs during training

* [GUI] Add loss type selection to analysis graph

* Fix store command name in recent files. Switch to correct tab on open

* [GUI] Disable training graph when 'no-logs' is selected

* Fix graphing race condition

* rename original_hires model to unbalanced" class="Link--secondary" href="/borisdayma/faceswap/commit/cd00859c40a4bf94cbab0583882cc23a67c87e67">model_refactor (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="395206121" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/571" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/571/hovercard" href="https://github.com/deepfakes/faceswap/pull/571">deepfakes#571</a><a data-pjax="true" title="model_refactor (#571) (#572)

* model_refactor (#571)

* original model to new structure

* IAE model to new structure

* OriginalHiRes to new structure

* Fix trainer for different resolutions

* Initial config implementation

* Configparse library added

* improved training data loader

* dfaker model working

* Add logging to training functions

* Non blocking input for cli training

* Add error handling to threads. Add non-mp queues to queue_handler

* Improved Model Building and NNMeta

* refactor lib/models

* training refactor. DFL H128 model Implementation

* Dfaker - use hashes

* Move timelapse. Remove perceptual loss arg

* Update INSTALL.md. Add logger formatting. Update Dfaker training

* DFL h128 partially ported

* Add mask to dfaker (#573)

* Remove old models. Add mask to dfaker

* dfl mask. Make masks selectable in config (#575)

* DFL H128 Mask. Mask type selectable in config.

* remove gan_v2_2

* Creating Input Size config for models

Creating Input Size config for models

Will be used downstream in converters.

Also name change of image_shape to input_shape to clarify ( for future models with potentially different output_shapes)

* Add mask loss options to config

* MTCNN options to config.ini. Remove GAN config. Update USAGE.md

* Add sliders for numerical values in GUI

* Add config plugins menu to gui. Validate config

* Only backup model if loss has dropped. Get training working again

* bugfixes

* Standardise loss printing

* GUI idle cpu fixes. Graph loss fix.

* mutli-gpu logging bugfix

* Merge branch 'staging' into train_refactor

* backup state file

* Crash protection: Only backup if both total losses have dropped

* Port OriginalHiRes_RC4 to train_refactor (OriginalHiRes)

* Load and save model structure with weights

* Slight code update

* Improve config loader. Add subpixel opt to all models. Config to state

* Show samples... wrong input

* Remove AE topology. Add input/output shapes to State

* Port original_villain (birb/VillainGuy) model to faceswap

* Add plugin info to GUI config pages

* Load input shape from state. IAE Config options.

* Fix transform_kwargs.
Coverage to ratio.
Bugfix mask detection

* Suppress keras userwarnings.
Automate zoom.
Coverage_ratio to model def.

* Consolidation of converters &amp; refactor (#574)

* Consolidation of converters &amp; refactor

Initial Upload of alpha

Items
- consolidate convert_mased &amp; convert_adjust into one converter
-add average color adjust to convert_masked
-allow mask transition blur size to be a fixed integer of pixels and a fraction of the facial mask size
-allow erosion/dilation size to be a fixed integer of pixels and a fraction of the facial mask size
-eliminate redundant type conversions to avoid multiple round-off errors
-refactor loops for vectorization/speed
-reorganize for clarity &amp; style changes

TODO
- bug/issues with warping the new face onto a transparent old image...use a cleanup mask for now
- issues with mask border giving black ring at zero erosion .. investigate
- remove GAN ??
- test enlargment factors of umeyama standard face .. match to coverage factor
- make enlargment factor a model parameter
- remove convert_adjusted and referencing code when finished

* Update Convert_Masked.py

default blur size of 2 to match original...
description of enlargement tests
breakout matrxi scaling into def

* Enlargment scale as a cli parameter

* Update cli.py

* dynamic interpolation algorithm

Compute x &amp; y scale factors from the affine matrix on the fly by QR decomp.
Choose interpolation alogrithm for the affine warp based on an upsample or downsample for each image

* input size
input size from config

* fix issues with &lt;1.0 erosion

* Update convert.py

* Update Convert_Adjust.py

more work on the way to merginf

* Clean up help note on sharpen

* cleanup seamless

* Delete Convert_Adjust.py

* Update umeyama.py

* Update training_data.py

* swapping

* segmentation stub

* changes to convert.str

* Update masked.py

* Backwards compatibility fix for models
Get converter running

* Convert:
Move masks to class.
bugfix blur_size
some linting

* mask fix

* convert fixes

- missing facehull_rect re-added
- coverage to %
- corrected coverage logic
- cleanup of gui option ordering

* Update cli.py

* default for blur

* Update masked.py

* added preliminary low_mem version of OriginalHighRes model plugin

* Code cleanup, minor fixes

* Update masked.py

* Update masked.py

* Add dfl mask to convert

* histogram fix &amp; seamless location

* update

* revert

* bugfix: Load actual configuration in gui

* Standardize nn_blocks

* Update cli.py

* Minor code amends

* Fix Original HiRes model

* Add masks to preview output for mask trainers
refactor trainer.__base.py

* Masked trainers converter support

* convert bugfix

* Bugfix: Converter for masked (dfl/dfaker) trainers

* Additional Losses (#592)

* initial upload

* Delete blur.py

* default initializer = He instead of Glorot (#588)

* Allow kernel_initializer to be overridable

* Add ICNR Initializer option for upscale on all models.

* Hopefully fixes RSoDs with original-highres model plugin

* remove debug line

* Original-HighRes model plugin Red Screen of Death fix, take #2

* Move global options to _base. Rename Villain model

* clipnorm and res block biases

* scale the end of res block

* res block

* dfaker pre-activation res

* OHRES pre-activation

* villain pre-activation

* tabs/space in nn_blocks

* fix for histogram with mask all set to zero

* fix to prevent two networks with same name

* GUI: Wider tooltips. Improve TQDM capture

* Fix regex bug

* Convert padding=48 to ratio of image size

* Add size option to alignments tool extract

* Pass through training image size to convert from model

* Convert: Pull training coverage from model

* convert: coverage, blur and erode to percent

* simplify matrix scaling

* ordering of sliders in train

* Add matrix scaling to utils. Use interpolation in lib.aligner transform

* masked.py Import get_matrix_scaling from utils

* fix circular import

* Update masked.py

* quick fix for matrix scaling

* testing thus for now

* tqdm regex capture bugfix

* Minor ammends

* blur size cleanup

* Remove coverage option from convert (Now cascades from model)

* Implement convert for all model types

* Add mask option and coverage option to all existing models

* bugfix for model loading on convert

* debug print removal

* Bugfix for masks in dfl_h128 and iae

* Update preview display. Add preview scaling to cli

* mask notes

* Delete training_data_v2.py

errant file

* training data variables

* Fix timelapse function

* Add new config items to state file for legacy purposes

* Slight GUI tweak

* Raise exception if problem with loaded model

* Add Tensorboard support (Logs stored in model directory)

* ICNR fix

* loss bugfix

* convert bugfix

* Move ini files to config folder. Make TensorBoard optional

* Fix training data for unbalanced inputs/outputs

* Fix config &quot;none&quot; test

* Keep helptext in .ini files when saving config from GUI

* Remove frame_dims from alignments

* Add no-flip and warp-to-landmarks cli options

* Revert OHR to RC4_fix version

* Fix lowmem mode on OHR model

* padding to variable

* Save models in parallel threads

* Speed-up of res_block stability

* Automated Reflection Padding

* Reflect Padding as a training option

Includes auto-calculation of proper padding shapes, input_shapes, output_shapes

Flag included in config now

* rest of reflect padding

* Move TB logging to cli. Session info to state file

* Add session iterations to state file

* Add recent files to menu. GUI code tidy up

* [GUI] Fix recent file list update issue

* Add correct loss names to TensorBoard logs

* Update live graph to use TensorBoard and remove animation

* Fix analysis tab. GUI optimizations

* Analysis Graph popup to Tensorboard Logs

* [GUI] Bug fix for graphing for models with hypens in name

* [GUI] Correctly split loss to tabs during training

* [GUI] Add loss type selection to analysis graph

* Fix store command name in recent files. Switch to correct tab on open

* [GUI] Disable training graph when 'no-logs' is selected

* Fix graphing race condition

* rename original_hires model to unbalanced" class="Link--secondary" href="/borisdayma/faceswap/commit/cd00859c40a4bf94cbab0583882cc23a67c87e67">) (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="395208673" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/572" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/572/hovercard" href="https://github.com/deepfakes/faceswap/pull/572">deepfakes#572</a><a data-pjax="true" title="model_refactor (#571) (#572)

* model_refactor (#571)

* original model to new structure

* IAE model to new structure

* OriginalHiRes to new structure

* Fix trainer for different resolutions

* Initial config implementation

* Configparse library added

* improved training data loader

* dfaker model working

* Add logging to training functions

* Non blocking input for cli training

* Add error handling to threads. Add non-mp queues to queue_handler

* Improved Model Building and NNMeta

* refactor lib/models

* training refactor. DFL H128 model Implementation

* Dfaker - use hashes

* Move timelapse. Remove perceptual loss arg

* Update INSTALL.md. Add logger formatting. Update Dfaker training

* DFL h128 partially ported

* Add mask to dfaker (#573)

* Remove old models. Add mask to dfaker

* dfl mask. Make masks selectable in config (#575)

* DFL H128 Mask. Mask type selectable in config.

* remove gan_v2_2

* Creating Input Size config for models

Creating Input Size config for models

Will be used downstream in converters.

Also name change of image_shape to input_shape to clarify ( for future models with potentially different output_shapes)

* Add mask loss options to config

* MTCNN options to config.ini. Remove GAN config. Update USAGE.md

* Add sliders for numerical values in GUI

* Add config plugins menu to gui. Validate config

* Only backup model if loss has dropped. Get training working again

* bugfixes

* Standardise loss printing

* GUI idle cpu fixes. Graph loss fix.

* mutli-gpu logging bugfix

* Merge branch 'staging' into train_refactor

* backup state file

* Crash protection: Only backup if both total losses have dropped

* Port OriginalHiRes_RC4 to train_refactor (OriginalHiRes)

* Load and save model structure with weights

* Slight code update

* Improve config loader. Add subpixel opt to all models. Config to state

* Show samples... wrong input

* Remove AE topology. Add input/output shapes to State

* Port original_villain (birb/VillainGuy) model to faceswap

* Add plugin info to GUI config pages

* Load input shape from state. IAE Config options.

* Fix transform_kwargs.
Coverage to ratio.
Bugfix mask detection

* Suppress keras userwarnings.
Automate zoom.
Coverage_ratio to model def.

* Consolidation of converters &amp; refactor (#574)

* Consolidation of converters &amp; refactor

Initial Upload of alpha

Items
- consolidate convert_mased &amp; convert_adjust into one converter
-add average color adjust to convert_masked
-allow mask transition blur size to be a fixed integer of pixels and a fraction of the facial mask size
-allow erosion/dilation size to be a fixed integer of pixels and a fraction of the facial mask size
-eliminate redundant type conversions to avoid multiple round-off errors
-refactor loops for vectorization/speed
-reorganize for clarity &amp; style changes

TODO
- bug/issues with warping the new face onto a transparent old image...use a cleanup mask for now
- issues with mask border giving black ring at zero erosion .. investigate
- remove GAN ??
- test enlargment factors of umeyama standard face .. match to coverage factor
- make enlargment factor a model parameter
- remove convert_adjusted and referencing code when finished

* Update Convert_Masked.py

default blur size of 2 to match original...
description of enlargement tests
breakout matrxi scaling into def

* Enlargment scale as a cli parameter

* Update cli.py

* dynamic interpolation algorithm

Compute x &amp; y scale factors from the affine matrix on the fly by QR decomp.
Choose interpolation alogrithm for the affine warp based on an upsample or downsample for each image

* input size
input size from config

* fix issues with &lt;1.0 erosion

* Update convert.py

* Update Convert_Adjust.py

more work on the way to merginf

* Clean up help note on sharpen

* cleanup seamless

* Delete Convert_Adjust.py

* Update umeyama.py

* Update training_data.py

* swapping

* segmentation stub

* changes to convert.str

* Update masked.py

* Backwards compatibility fix for models
Get converter running

* Convert:
Move masks to class.
bugfix blur_size
some linting

* mask fix

* convert fixes

- missing facehull_rect re-added
- coverage to %
- corrected coverage logic
- cleanup of gui option ordering

* Update cli.py

* default for blur

* Update masked.py

* added preliminary low_mem version of OriginalHighRes model plugin

* Code cleanup, minor fixes

* Update masked.py

* Update masked.py

* Add dfl mask to convert

* histogram fix &amp; seamless location

* update

* revert

* bugfix: Load actual configuration in gui

* Standardize nn_blocks

* Update cli.py

* Minor code amends

* Fix Original HiRes model

* Add masks to preview output for mask trainers
refactor trainer.__base.py

* Masked trainers converter support

* convert bugfix

* Bugfix: Converter for masked (dfl/dfaker) trainers

* Additional Losses (#592)

* initial upload

* Delete blur.py

* default initializer = He instead of Glorot (#588)

* Allow kernel_initializer to be overridable

* Add ICNR Initializer option for upscale on all models.

* Hopefully fixes RSoDs with original-highres model plugin

* remove debug line

* Original-HighRes model plugin Red Screen of Death fix, take #2

* Move global options to _base. Rename Villain model

* clipnorm and res block biases

* scale the end of res block

* res block

* dfaker pre-activation res

* OHRES pre-activation

* villain pre-activation

* tabs/space in nn_blocks

* fix for histogram with mask all set to zero

* fix to prevent two networks with same name

* GUI: Wider tooltips. Improve TQDM capture

* Fix regex bug

* Convert padding=48 to ratio of image size

* Add size option to alignments tool extract

* Pass through training image size to convert from model

* Convert: Pull training coverage from model

* convert: coverage, blur and erode to percent

* simplify matrix scaling

* ordering of sliders in train

* Add matrix scaling to utils. Use interpolation in lib.aligner transform

* masked.py Import get_matrix_scaling from utils

* fix circular import

* Update masked.py

* quick fix for matrix scaling

* testing thus for now

* tqdm regex capture bugfix

* Minor ammends

* blur size cleanup

* Remove coverage option from convert (Now cascades from model)

* Implement convert for all model types

* Add mask option and coverage option to all existing models

* bugfix for model loading on convert

* debug print removal

* Bugfix for masks in dfl_h128 and iae

* Update preview display. Add preview scaling to cli

* mask notes

* Delete training_data_v2.py

errant file

* training data variables

* Fix timelapse function

* Add new config items to state file for legacy purposes

* Slight GUI tweak

* Raise exception if problem with loaded model

* Add Tensorboard support (Logs stored in model directory)

* ICNR fix

* loss bugfix

* convert bugfix

* Move ini files to config folder. Make TensorBoard optional

* Fix training data for unbalanced inputs/outputs

* Fix config &quot;none&quot; test

* Keep helptext in .ini files when saving config from GUI

* Remove frame_dims from alignments

* Add no-flip and warp-to-landmarks cli options

* Revert OHR to RC4_fix version

* Fix lowmem mode on OHR model

* padding to variable

* Save models in parallel threads

* Speed-up of res_block stability

* Automated Reflection Padding

* Reflect Padding as a training option

Includes auto-calculation of proper padding shapes, input_shapes, output_shapes

Flag included in config now

* rest of reflect padding

* Move TB logging to cli. Session info to state file

* Add session iterations to state file

* Add recent files to menu. GUI code tidy up

* [GUI] Fix recent file list update issue

* Add correct loss names to TensorBoard logs

* Update live graph to use TensorBoard and remove animation

* Fix analysis tab. GUI optimizations

* Analysis Graph popup to Tensorboard Logs

* [GUI] Bug fix for graphing for models with hypens in name

* [GUI] Correctly split loss to tabs during training

* [GUI] Add loss type selection to analysis graph

* Fix store command name in recent files. Switch to correct tab on open

* [GUI] Disable training graph when 'no-logs' is selected

* Fix graphing race condition

* rename original_hires model to unbalanced" class="Link--secondary" href="/borisdayma/faceswap/commit/cd00859c40a4bf94cbab0583882cc23a67c87e67">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-02-09T18:35:12Z" data-view-component="true" class="no-wrap">Feb 9, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="docs" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/docs">docs</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Optimize Data Augmentation (#881)

* Move image utils to lib.image
* Add .pylintrc file
* Remove some cv2 pylint ignores
* TrainingData: Load images from disk in batches
* TrainingData: get_landmarks to batch
* TrainingData: transform and flip to batches
* TrainingData: Optimize color augmentation
* TrainingData: Optimize target and random_warp
* TrainingData - Convert _get_closest_match for batching
* TrainingData: Warp To Landmarks optimized
* Save models to threadpoolexecutor
* Move stack_images, Rename ImageManipulation. ImageAugmentation Docstrings
* Masks: Set dtype and threshold for lib.masks based on input face
* Docstrings and Documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/66ed005ef3d824b4f8221f7fe5019ffca770a94e">Optimize Data Augmentation (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="497388562" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/881" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/881/hovercard" href="https://github.com/deepfakes/faceswap/pull/881">deepfakes#881</a><a data-pjax="true" title="Optimize Data Augmentation (#881)

* Move image utils to lib.image
* Add .pylintrc file
* Remove some cv2 pylint ignores
* TrainingData: Load images from disk in batches
* TrainingData: get_landmarks to batch
* TrainingData: transform and flip to batches
* TrainingData: Optimize color augmentation
* TrainingData: Optimize target and random_warp
* TrainingData - Convert _get_closest_match for batching
* TrainingData: Warp To Landmarks optimized
* Save models to threadpoolexecutor
* Move stack_images, Rename ImageManipulation. ImageAugmentation Docstrings
* Masks: Set dtype and threshold for lib.masks based on input face
* Docstrings and Documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/66ed005ef3d824b4f8221f7fe5019ffca770a94e">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-24T11:16:05Z" data-view-component="true" class="no-wrap">Sep 24, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="lib" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/lib">lib</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Fix graph pop up" class="Link--secondary" href="/borisdayma/faceswap/commit/c2e54bb18a9852ce0406e3b845554f51efb30558">Fix graph pop up</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-25T18:31:32Z" data-view-component="true" class="no-wrap">Sep 25, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="plugins" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/plugins">plugins</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Logging format fixes" class="Link--secondary" href="/borisdayma/faceswap/commit/174e6950ea6ced56efd26c8188ba645e2fa4ac36">Logging format fixes</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-25T12:01:24Z" data-view-component="true" class="no-wrap">Sep 25, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="scripts" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/scripts">scripts</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Logging format fixes" class="Link--secondary" href="/borisdayma/faceswap/commit/174e6950ea6ced56efd26c8188ba645e2fa4ac36">Logging format fixes</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-25T12:01:24Z" data-view-component="true" class="no-wrap">Sep 25, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <path d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3H7.5a.25.25 0 01-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="tools" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tree/master/tools">tools</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Alignments tool: Remove extract-large and add `large` option" class="Link--secondary" href="/borisdayma/faceswap/commit/46efae3506ffd31900a70887b75b5a795f02d52d">Alignments tool: Remove extract-large and add <code>large</code> option</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-26T17:22:22Z" data-view-component="true" class="no-wrap">Sep 26, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title=".dockerignore" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/.dockerignore">.dockerignore</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Clearer requirements for each platform (#183)" class="Link--secondary" href="/borisdayma/faceswap/commit/0085b5b8a7987a2bcc862d27b474ca6dc58e2ef8">Clearer requirements for each platform (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="296207203" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/183" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/183/hovercard" href="https://github.com/deepfakes/faceswap/pull/183">deepfakes#183</a><a data-pjax="true" title="Clearer requirements for each platform (#183)" class="Link--secondary" href="/borisdayma/faceswap/commit/0085b5b8a7987a2bcc862d27b474ca6dc58e2ef8">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2018-02-14T15:22:02Z" data-view-component="true" class="no-wrap">Feb 14, 2018</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title=".gitignore" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/.gitignore">.gitignore</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Optimize Data Augmentation (#881)

* Move image utils to lib.image
* Add .pylintrc file
* Remove some cv2 pylint ignores
* TrainingData: Load images from disk in batches
* TrainingData: get_landmarks to batch
* TrainingData: transform and flip to batches
* TrainingData: Optimize color augmentation
* TrainingData: Optimize target and random_warp
* TrainingData - Convert _get_closest_match for batching
* TrainingData: Warp To Landmarks optimized
* Save models to threadpoolexecutor
* Move stack_images, Rename ImageManipulation. ImageAugmentation Docstrings
* Masks: Set dtype and threshold for lib.masks based on input face
* Docstrings and Documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/66ed005ef3d824b4f8221f7fe5019ffca770a94e">Optimize Data Augmentation (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="497388562" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/881" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/881/hovercard" href="https://github.com/deepfakes/faceswap/pull/881">deepfakes#881</a><a data-pjax="true" title="Optimize Data Augmentation (#881)

* Move image utils to lib.image
* Add .pylintrc file
* Remove some cv2 pylint ignores
* TrainingData: Load images from disk in batches
* TrainingData: get_landmarks to batch
* TrainingData: transform and flip to batches
* TrainingData: Optimize color augmentation
* TrainingData: Optimize target and random_warp
* TrainingData - Convert _get_closest_match for batching
* TrainingData: Warp To Landmarks optimized
* Save models to threadpoolexecutor
* Move stack_images, Rename ImageManipulation. ImageAugmentation Docstrings
* Masks: Set dtype and threshold for lib.masks based on input face
* Docstrings and Documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/66ed005ef3d824b4f8221f7fe5019ffca770a94e">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-24T11:16:05Z" data-view-component="true" class="no-wrap">Sep 24, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title=".pylintrc" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/.pylintrc">.pylintrc</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Optimize Data Augmentation (#881)

* Move image utils to lib.image
* Add .pylintrc file
* Remove some cv2 pylint ignores
* TrainingData: Load images from disk in batches
* TrainingData: get_landmarks to batch
* TrainingData: transform and flip to batches
* TrainingData: Optimize color augmentation
* TrainingData: Optimize target and random_warp
* TrainingData - Convert _get_closest_match for batching
* TrainingData: Warp To Landmarks optimized
* Save models to threadpoolexecutor
* Move stack_images, Rename ImageManipulation. ImageAugmentation Docstrings
* Masks: Set dtype and threshold for lib.masks based on input face
* Docstrings and Documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/66ed005ef3d824b4f8221f7fe5019ffca770a94e">Optimize Data Augmentation (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="497388562" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/881" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/881/hovercard" href="https://github.com/deepfakes/faceswap/pull/881">deepfakes#881</a><a data-pjax="true" title="Optimize Data Augmentation (#881)

* Move image utils to lib.image
* Add .pylintrc file
* Remove some cv2 pylint ignores
* TrainingData: Load images from disk in batches
* TrainingData: get_landmarks to batch
* TrainingData: transform and flip to batches
* TrainingData: Optimize color augmentation
* TrainingData: Optimize target and random_warp
* TrainingData - Convert _get_closest_match for batching
* TrainingData: Warp To Landmarks optimized
* Save models to threadpoolexecutor
* Move stack_images, Rename ImageManipulation. ImageAugmentation Docstrings
* Masks: Set dtype and threshold for lib.masks based on input face
* Docstrings and Documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/66ed005ef3d824b4f8221f7fe5019ffca770a94e">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-24T11:16:05Z" data-view-component="true" class="no-wrap">Sep 24, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title=".travis.yml" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/.travis.yml">.travis.yml</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Add CONDA_BLD_PATH to travis again (derped)" class="Link--secondary" href="/borisdayma/faceswap/commit/088c8389cc2a5723a3bdd575b25536e58fd669c1">Add CONDA_BLD_PATH to travis again (derped)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-22T18:23:43Z" data-view-component="true" class="no-wrap">Sep 22, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="CODE_OF_CONDUCT.md" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/CODE_OF_CONDUCT.md">CODE_OF_CONDUCT.md</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Analysis Fixups

- Move stats calculations to LongRunningTasks
- Fix divide by zero error on rate calculations" class="Link--secondary" href="/borisdayma/faceswap/commit/ebea2b7142c1d9989cb2dd2dac03515dd8cdffe5">Analysis Fixups</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-06-27T17:27:47Z" data-view-component="true" class="no-wrap">Jun 27, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="Dockerfile.cpu" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/Dockerfile.cpu">Dockerfile.cpu</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="add git to dockerfiles (#839)" class="Link--secondary" href="/borisdayma/faceswap/commit/6c1a97aef2bd9aa446cc6d215788598faccea684">add git to dockerfiles (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="482557808" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/839" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/839/hovercard" href="https://github.com/deepfakes/faceswap/pull/839">deepfakes#839</a><a data-pjax="true" title="add git to dockerfiles (#839)" class="Link--secondary" href="/borisdayma/faceswap/commit/6c1a97aef2bd9aa446cc6d215788598faccea684">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-08-19T22:33:21Z" data-view-component="true" class="no-wrap">Aug 19, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="Dockerfile.gpu" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/Dockerfile.gpu">Dockerfile.gpu</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="add git to dockerfiles (#839)" class="Link--secondary" href="/borisdayma/faceswap/commit/6c1a97aef2bd9aa446cc6d215788598faccea684">add git to dockerfiles (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="482557808" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/839" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/839/hovercard" href="https://github.com/deepfakes/faceswap/pull/839">deepfakes#839</a><a data-pjax="true" title="add git to dockerfiles (#839)" class="Link--secondary" href="/borisdayma/faceswap/commit/6c1a97aef2bd9aa446cc6d215788598faccea684">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-08-19T22:33:21Z" data-view-component="true" class="no-wrap">Aug 19, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="INSTALL.md" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/INSTALL.md">INSTALL.md</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Update links to faceswap.dev/forum" class="Link--secondary" href="/borisdayma/faceswap/commit/76783ddc4ea75e5ad35f671cae6f49507d0a5b8d">Update links to faceswap.dev/forum</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-07-13T08:08:09Z" data-view-component="true" class="no-wrap">Jul 13, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="LICENSE" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" itemprop="license" href="/borisdayma/faceswap/blob/master/LICENSE">LICENSE</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Add GNU General Public License v3.0" class="Link--secondary" href="/borisdayma/faceswap/commit/02ac46ec5ae09c25cbeaaae5f323550a7a4ea27c">Add GNU General Public License v3.0</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2018-02-25T16:41:32Z" data-view-component="true" class="no-wrap">Feb 25, 2018</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="README.md" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/README.md">README.md</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Add docs build badge to README.md" class="Link--secondary" href="/borisdayma/faceswap/commit/97dc8c13f3f61912c706767429c5bcba6febf883">Add docs build badge to README.md</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-16T23:43:30Z" data-view-component="true" class="no-wrap">Sep 16, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="USAGE.md" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/USAGE.md">USAGE.md</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Update links to faceswap.dev/forum" class="Link--secondary" href="/borisdayma/faceswap/commit/76783ddc4ea75e5ad35f671cae6f49507d0a5b8d">Update links to faceswap.dev/forum</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-07-13T08:08:09Z" data-view-component="true" class="no-wrap">Jul 13, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="_config.yml" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/_config.yml">_config.yml</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Set theme jekyll-theme-cayman" class="Link--secondary" href="/borisdayma/faceswap/commit/a76671de471ca8b55c37070c121b320bfc4580c8">Set theme jekyll-theme-cayman</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-07-31T00:46:12Z" data-view-component="true" class="no-wrap">Jul 31, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="faceswap.py" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/faceswap.py">faceswap.py</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Gui v3.0b (#436)

* GUI version 3 (#411)

GUI version 3.0a

* Required for Shaonlu mode (#416)

Added two modes - Original and Shaonlu.
The later requires this file to function.

* model update (#417)

New, functional Original 128 model

* OriginalHighRes 128 model update (#418)

Required for OriginalHighRes Model to function

* Add OriginalHighRes 128 update to gui branch (#421)

* Required for Shaonlu mode (#416)

Added two modes - Original and Shaonlu.
The later requires this file to function.

* model update (#417)

New, functional Original 128 model

* OriginalHighRes 128 model update (#418)

Required for OriginalHighRes Model to function

* Dev gui (#420)

* reduce singletons

* Fix tooltips and screen boundaries on popup

* Remove dpi fix. Fix context filebrowsers

* fix tools.py execution and context filebrowser bugs

* Bugfixes (#422)

* Bump matplotlib requirement. Fix polyfit. Fix TQDM on sort

* Fixed memory usage at 6GB cards. (#423)

- Switched default encoder to ORIGINAL
- Fixed memory consumption. Tested with geforce gtx 9800 ti with 6Gb; batch_size 8 no OOM or memory warnings now.

* Staging (#426)

* altered trainer (#425)

altered trainer to accommodate with model change

* Update Model.py (#424)

- Added saving state (currently only saved epoch number, to be extended in future)
- Changed saving to ThreadPoolExecutor

* Add DPI Scaling (#428)

* Add dpi scaling

* Hotfix for effmpeg. (#429)

effmpeg fixed so it works both in cli and gui.
Initial work done to add previewing feature to effmpeg (currently does nothing).
Some small spacing changes in other files to improve PEP8 conformity.

* PEP8 Linting (#430)

* pep8 linting

* Requirements version bump (#432)

* altered trainer (#425)

altered trainer to accommodate with model change

* Update Model.py (#424)

- Added saving state (currently only saved epoch number, to be extended in future)
- Changed saving to ThreadPoolExecutor

* Requirements version bump (#431)

This bumps the versions of:

    scandir
    h5py
    Keras
    opencv-python

to their latest vesions.

Virtual Environment will need to be setup again to make use of these.

* High DPI Fixes (#433)

* dpi scaling

* DPI Fixes

* Fix and improve context manager. (#434)

effmpeg tool:
Context manager for GUI fixed.

Context manager in general:
Functionality extended to allow configuring the context with both:
  command -&gt; action
  command -&gt; variable (cli argument) -&gt; action

* Change epoch option to iterations

* Change epochs to iterations" class="Link--secondary" href="/borisdayma/faceswap/commit/be8e235eab61ec6c72d0213250efea2908ed8452">Gui v3.0b (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="334178040" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/436" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/436/hovercard" href="https://github.com/deepfakes/faceswap/pull/436">deepfakes#436</a><a data-pjax="true" title="Gui v3.0b (#436)

* GUI version 3 (#411)

GUI version 3.0a

* Required for Shaonlu mode (#416)

Added two modes - Original and Shaonlu.
The later requires this file to function.

* model update (#417)

New, functional Original 128 model

* OriginalHighRes 128 model update (#418)

Required for OriginalHighRes Model to function

* Add OriginalHighRes 128 update to gui branch (#421)

* Required for Shaonlu mode (#416)

Added two modes - Original and Shaonlu.
The later requires this file to function.

* model update (#417)

New, functional Original 128 model

* OriginalHighRes 128 model update (#418)

Required for OriginalHighRes Model to function

* Dev gui (#420)

* reduce singletons

* Fix tooltips and screen boundaries on popup

* Remove dpi fix. Fix context filebrowsers

* fix tools.py execution and context filebrowser bugs

* Bugfixes (#422)

* Bump matplotlib requirement. Fix polyfit. Fix TQDM on sort

* Fixed memory usage at 6GB cards. (#423)

- Switched default encoder to ORIGINAL
- Fixed memory consumption. Tested with geforce gtx 9800 ti with 6Gb; batch_size 8 no OOM or memory warnings now.

* Staging (#426)

* altered trainer (#425)

altered trainer to accommodate with model change

* Update Model.py (#424)

- Added saving state (currently only saved epoch number, to be extended in future)
- Changed saving to ThreadPoolExecutor

* Add DPI Scaling (#428)

* Add dpi scaling

* Hotfix for effmpeg. (#429)

effmpeg fixed so it works both in cli and gui.
Initial work done to add previewing feature to effmpeg (currently does nothing).
Some small spacing changes in other files to improve PEP8 conformity.

* PEP8 Linting (#430)

* pep8 linting

* Requirements version bump (#432)

* altered trainer (#425)

altered trainer to accommodate with model change

* Update Model.py (#424)

- Added saving state (currently only saved epoch number, to be extended in future)
- Changed saving to ThreadPoolExecutor

* Requirements version bump (#431)

This bumps the versions of:

    scandir
    h5py
    Keras
    opencv-python

to their latest vesions.

Virtual Environment will need to be setup again to make use of these.

* High DPI Fixes (#433)

* dpi scaling

* DPI Fixes

* Fix and improve context manager. (#434)

effmpeg tool:
Context manager for GUI fixed.

Context manager in general:
Functionality extended to allow configuring the context with both:
  command -&gt; action
  command -&gt; variable (cli argument) -&gt; action

* Change epoch option to iterations

* Change epochs to iterations" class="Link--secondary" href="/borisdayma/faceswap/commit/be8e235eab61ec6c72d0213250efea2908ed8452">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2018-06-20T17:25:31Z" data-view-component="true" class="no-wrap">Jun 20, 2018</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="requirements.txt" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/requirements.txt">requirements.txt</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="De-Multiprocess Extract (#871)

* requirements.txt: - Pin opencv to 4.1.1 (fixes cv2-dnn error)

* lib.face_detect.DetectedFace: change LandmarksXY to landmarks_xy. Add left, right, top, bottom attributes

* lib.model.session: Session manager for loading models into different graphs (for Nvidia + CPU)

* plugins.extract._base: New parent class for all extract plugins

* plugins.extract.pipeline. Remove MultiProcessing. Dynamically limit batchsize for Nvidia cards. Remove loglevel input

* S3FD + FAN plugins. Standardise to Keras version for all backends

* Standardize all extract plugins to new threaded codebase

* Documentation. Start implementing Numpy style docstrings for Sphinx Documentation

* Remove s3fd_amd. Change convert OTF to expect DetectedFace object

* faces_detect - clean up and documentation

* Remove PoolProcess

* Migrate manual tool to new extract workflow

* Remove AMD specific extractor code from cli and plugins

* Sort tool to new extract workflow

* Remove multiprocessing from project

* Remove multiprocessing queues from QueueManager

* Remove multiprocessing support from logger

* Move face_filter to new extraction pipeline

* Alignments landmarksXY &gt; landmarks_xy and legacy handling

* Intercept get_backend for sphinx doc build

# Add Sphinx documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/88352b0268efe49b54c9bdfad4846317752991ed">De-Multiprocess Extract (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="493676033" data-permission-text="Title is private" data-url="https://github.com/deepfakes/faceswap/issues/871" data-hovercard-type="pull_request" data-hovercard-url="/deepfakes/faceswap/pull/871/hovercard" href="https://github.com/deepfakes/faceswap/pull/871">deepfakes#871</a><a data-pjax="true" title="De-Multiprocess Extract (#871)

* requirements.txt: - Pin opencv to 4.1.1 (fixes cv2-dnn error)

* lib.face_detect.DetectedFace: change LandmarksXY to landmarks_xy. Add left, right, top, bottom attributes

* lib.model.session: Session manager for loading models into different graphs (for Nvidia + CPU)

* plugins.extract._base: New parent class for all extract plugins

* plugins.extract.pipeline. Remove MultiProcessing. Dynamically limit batchsize for Nvidia cards. Remove loglevel input

* S3FD + FAN plugins. Standardise to Keras version for all backends

* Standardize all extract plugins to new threaded codebase

* Documentation. Start implementing Numpy style docstrings for Sphinx Documentation

* Remove s3fd_amd. Change convert OTF to expect DetectedFace object

* faces_detect - clean up and documentation

* Remove PoolProcess

* Migrate manual tool to new extract workflow

* Remove AMD specific extractor code from cli and plugins

* Sort tool to new extract workflow

* Remove multiprocessing from project

* Remove multiprocessing queues from QueueManager

* Remove multiprocessing support from logger

* Move face_filter to new extraction pipeline

* Alignments landmarksXY &gt; landmarks_xy and legacy handling

* Intercept get_backend for sphinx doc build

# Add Sphinx documentation" class="Link--secondary" href="/borisdayma/faceswap/commit/88352b0268efe49b54c9bdfad4846317752991ed">)</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-09-15T16:07:41Z" data-view-component="true" class="no-wrap">Sep 15, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="setup.cfg" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/setup.cfg">setup.cfg</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="dlib-cnn: Inconsistent image size bugfix" class="Link--secondary" href="/borisdayma/faceswap/commit/bfdae74f669985d42304c2a4044d027efb4a57e8">dlib-cnn: Inconsistent image size bugfix</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2018-11-12T12:30:08Z" data-view-component="true" class="no-wrap">Nov 12, 2018</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="setup.py" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/setup.py">setup.py</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="More seamless AMD Integration

- utils.py: Set FS backend if .faceswap config file doesn&#39;t exist
- setup.py: set .faceswap config on setup
- Dynamically load options for AMD/CPU/NVIDIA backends" class="Link--secondary" href="/borisdayma/faceswap/commit/b8598be2b68a6d11b81d871d6bf453809a7cdd5e">More seamless AMD Integration</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-08-17T19:16:43Z" data-view-component="true" class="no-wrap">Aug 17, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="tools.py" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/tools.py">tools.py</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Add Restore Model Tool

Tool: Add tool to restore models from backup
Snapshot: Create snapshot based on total iterations rather than session iterations
Models: Move backup/snapshot functions to lib/model
Training: Output average loss since last save at each save iteration
GUI: display_page.py: minor logging update" class="Link--secondary" href="/borisdayma/faceswap/commit/e1fca147161a556109628f73ebba96c7ce7dc1f8">Add Restore Model Tool</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-07-01T23:28:31Z" data-view-component="true" class="no-wrap">Jul 1, 2019</time-ago>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="update_deps.py" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/blob/master/update_deps.py">update_deps.py</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <span class="css-truncate css-truncate-target d-block width-fit markdown-title">
                    <a data-pjax="true" title="Fixups

Dependency Updater: Improve by pluging in to setup.py
setup.py: Bugfix handling of Conda aliases
GUI: Revert console background colour
sysinfo: Handle errors in obtaining information" class="Link--secondary" href="/borisdayma/faceswap/commit/76d18c87d7b5e939bc67b4c3a5705434e8ac9bbe">Fixups</a>
              </span>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <time-ago datetime="2019-07-03T11:07:21Z" data-view-component="true" class="no-wrap">Jul 3, 2019</time-ago>
          </div>

        </div>
    </div>
    <div class="Details-content--shown Box-footer d-md-none p-0">
        <button aria-expanded="false" type="button" data-view-component="true" class="js-details-target btn-link d-block width-full px-3 py-2">    View code
</button>    </div>
  </div>




</div>

  
      <readme-toc>

      <div id="readme" class="Box md js-code-block-container js-code-nav-container js-tagsearch-file Box--responsive"
          data-tagsearch-path="README.md"
          data-tagsearch-lang="Markdown">

        <div class="d-flex  js-sticky js-position-sticky top-0 border-top-0 border-bottom p-2 flex-items-center flex-justify-between color-bg-default rounded-top-2"  style="position: sticky; z-index: 30;" >
          <div class="d-flex flex-items-center">
              <details
  data-target="readme-toc.trigger"
  data-menu-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;trigger&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}"
  data-menu-hydro-click-hmac="bbc2c8890a5fc009a5a14ff69589b32345818e9cc84c9c276f85cbb810dd7d79"
  class="dropdown details-reset details-overlay"
>
  <summary
    class="btn btn-octicon m-0 mr-2 p-2"
    aria-haspopup="true"
    aria-label="Table of Contents">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered">
    <path fill-rule="evenodd" d="M2 4a1 1 0 100-2 1 1 0 000 2zm3.75-1.5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zM3 8a1 1 0 11-2 0 1 1 0 012 0zm-1 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
  </summary>


  <details-menu class="SelectMenu" role="menu">
    <div class="SelectMenu-modal rounded-3 mt-1" style="max-height:340px;">

        <div class="SelectMenu-filter">
          <input
            class="SelectMenu-input form-control js-filterable-field"
            id="toc-filter-field"
            type="text"
            autocomplete="off"
            spellcheck="false"
            autofocus
            placeholder="Filter headings"
            aria-label="Filter headings">
        </div>

      <div class="SelectMenu-list SelectMenu-list--borderless p-2" style="overscroll-behavior: contain;" data-filterable-for="toc-filter-field" data-filterable-type="substring">
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#deepfakes_faceswap">deepfakes_faceswap</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#manifesto">Manifesto</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#faceswap-has-ethical-uses">FaceSwap has ethical uses.</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#how-to-setup-and-run-the-project">How To setup and run the project</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#overview">Overview</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#extract">Extract</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#train">Train</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#convert">Convert</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#gui">GUI</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#general-notes">General notes:</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#help-i-need-support">Help I need support!</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#discord-server">Discord Server</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#faceswap-forum">FaceSwap Forum</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#donate">Donate</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#patreon">Patreon</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#one-time-donations">One time Donations</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#torzdf">@torzdf</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#andenixa">@andenixa</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#kvrooman">@kvrooman</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#how-to-contribute">How to contribute</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#for-people-interested-in-the-generative-models">For people interested in the generative models</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#for-devs">For devs</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#for-non-dev-advanced-users">For non-dev advanced users</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#for-end-users">For end-users</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#for-haters">For haters</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#about-githubcomdeepfakes">About github.com/deepfakes</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#what-is-this-repo">What is this repo?</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#why-this-repo">Why this repo?</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#why-is-it-named-deepfakes-if-it-is-not-udeepfakes">Why is it named 'deepfakes' if it is not /u/deepfakes?</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#what-if-udeepfakes-feels-bad-about-that">What if /u/deepfakes feels bad about that?</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#about-machine-learning">About machine learning</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:211183970,&quot;originating_url&quot;:&quot;https://github.com/borisdayma/faceswap&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01d68d2557339d44652a439c2db71def16260a5d883eb75b4e020f473379d2b1" href="#how-does-a-computer-know-how-to-recognizeshape-faces-how-does-machine-learning-work-what-is-a-neural-network">How does a computer know how to recognize/shape faces? How does machine learning work? What is a neural network?</a>
      </div>
    </div>
  </details-menu>
</details>

            <h2 class="Box-title">
              <a href="#readme" data-view-component="true" class="Link--primary">README.md</a>
            </h2>
          </div>
        </div>

          <div data-target="readme-toc.content" class="Box-body px-5 pb-5">
            <article class="markdown-body entry-content container-lg" itemprop="text"><h1 dir="auto"><a id="user-content-deepfakes_faceswap" class="anchor" aria-hidden="true" href="#deepfakes_faceswap"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>deepfakes_faceswap</h1>
<p align="center" dir="auto">
  <a href="https://faceswap.dev" rel="nofollow"><img src="https://camo.githubusercontent.com/67e98a8ca1dde3d8f5d360ab52a581a905842e7056e5d8d147ae20a3f02024e3/68747470733a2f2f692e696d6775722e636f6d2f7a48766a486e622e706e67" data-canonical-src="https://i.imgur.com/zHvjHnb.png" style="max-width: 100%;"></a>
<br>FaceSwap is a tool that utilizes deep learning to recognize and swap faces in pictures and videos.
</p>
<p align="center" dir="auto">
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/56b72a8f58b9ec6df2734c9c2fdb016491d186f90809b66f0ed568a2ae169dd9/68747470733a2f2f692e696d6775722e636f6d2f6e5748464c44662e6a7067"><img src="https://camo.githubusercontent.com/56b72a8f58b9ec6df2734c9c2fdb016491d186f90809b66f0ed568a2ae169dd9/68747470733a2f2f692e696d6775722e636f6d2f6e5748464c44662e6a7067" data-canonical-src="https://i.imgur.com/nWHFLDf.jpg" style="max-width: 100%;"></a>
</p>
<p align="center" dir="auto">
<a href="https://www.patreon.com/bePatron?u=23238350" rel="nofollow"><img src="https://camo.githubusercontent.com/2b7105015397da52617ce6775a339b0b99d689d6f644c2ce911c5d472362bcbd/68747470733a2f2f63352e70617472656f6e2e636f6d2f65787465726e616c2f6c6f676f2f6265636f6d655f615f706174726f6e5f627574746f6e2e706e67" data-canonical-src="https://c5.patreon.com/external/logo/become_a_patron_button.png" style="max-width: 100%;"></a>
</p>
<p align="center" dir="auto">
  <a href="https://www.youtube.com/watch?v=r1jng79a5xc" rel="nofollow"><img src="https://camo.githubusercontent.com/4c8848e79bcc92e61653f11eafa8d97b316b6ec470a0eefd258700f407c3dc6b/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f72316a6e673739613578632f302e6a7067" data-canonical-src="https://img.youtube.com/vi/r1jng79a5xc/0.jpg" style="max-width: 100%;"></a>
<br>Jennifer Lawrence/Steve Buscemi FaceSwap using the Villain model
</p>
<p dir="auto"><a href="https://travis-ci.org/deepfakes/faceswap" rel="nofollow"><img src="https://camo.githubusercontent.com/5c360fbfef962f33d0441a38c6081389e9fb8a2291498d37ba421a1406efe9c8/68747470733a2f2f7472617669732d63692e6f72672f6465657066616b65732f66616365737761702e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://travis-ci.org/deepfakes/faceswap.svg?branch=master" style="max-width: 100%;"></a> <a href="https://faceswap.readthedocs.io/en/latest/?badge=latest" rel="nofollow"><img src="https://camo.githubusercontent.com/58b7e03bdd7d51e7d1729b3d6713709f2d204514deb36851d90afbbc75a2ac93/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f66616365737761702f62616467652f3f76657273696f6e3d6c6174657374" alt="Documentation Status" data-canonical-src="https://readthedocs.org/projects/faceswap/badge/?version=latest" style="max-width: 100%;"></a></p>
<p dir="auto">Make sure you check out <a href="/borisdayma/faceswap/blob/master/INSTALL.md">INSTALL.md</a> before getting started.</p>
<ul dir="auto">
<li><a href="#deepfakesfaceswap">deepfakes_faceswap</a></li>
<li><a href="#manifesto">Manifesto</a>
<ul dir="auto">
<li><a href="#faceswap-has-ethical-uses">FaceSwap has ethical uses.</a></li>
</ul>
</li>
<li><a href="#how-to-setup-and-run-the-project">How To setup and run the project</a></li>
<li><a href="#overview">Overview</a>
<ul dir="auto">
<li><a href="#extract">Extract</a></li>
<li><a href="#train">Train</a></li>
<li><a href="#convert">Convert</a></li>
<li><a href="#gui">GUI</a></li>
</ul>
</li>
<li><a href="#general-notes">General notes:</a></li>
<li><a href="#help-i-need-support">Help I need support!</a>
<ul dir="auto">
<li><a href="#discord-server">Discord Server</a></li>
<li><a href="#faceswap-forum">FaceSwap Forum</a></li>
</ul>
</li>
<li><a href="#donate">Donate</a>
<ul dir="auto">
<li><a href="#patreon">Patreon</a></li>
<li><a href="#one-time-donations">One time Donations</a>
<ul dir="auto">
<li><a href="#torzdf">@torzdf</a></li>
<li><a href="#andenixa">@andenixa</a></li>
<li><a href="#kvrooman">@kvrooman</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#how-to-contribute">How to contribute</a>
<ul dir="auto">
<li><a href="#for-people-interested-in-the-generative-models">For people interested in the generative models</a></li>
<li><a href="#for-devs">For devs</a></li>
<li><a href="#for-non-dev-advanced-users">For non-dev advanced users</a></li>
<li><a href="#for-end-users">For end-users</a></li>
<li><a href="#for-haters">For haters</a></li>
</ul>
</li>
<li><a href="#about-githubcomdeepfakes">About github.com/deepfakes</a>
<ul dir="auto">
<li><a href="#what-is-this-repo">What is this repo?</a></li>
<li><a href="#why-this-repo">Why this repo?</a></li>
<li><a href="#why-is-it-named-deepfakes-if-it-is-not-udeepfakes">Why is it named 'deepfakes' if it is not /u/deepfakes?</a></li>
<li><a href="#what-if-udeepfakes-feels-bad-about-that">What if /u/deepfakes feels bad about that?</a></li>
</ul>
</li>
<li><a href="#about-machine-learning">About machine learning</a>
<ul dir="auto">
<li><a href="#how-does-a-computer-know-how-to-recognizeshape-faces-how-does-machine-learning-work-what-is-a-neural-network">How does a computer know how to recognize/shape faces? How does machine learning work? What is a neural network?</a></li>
</ul>
</li>
</ul>
<h1 dir="auto"><a id="user-content-manifesto" class="anchor" aria-hidden="true" href="#manifesto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Manifesto</h1>
<h2 dir="auto"><a id="user-content-faceswap-has-ethical-uses" class="anchor" aria-hidden="true" href="#faceswap-has-ethical-uses"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>FaceSwap has ethical uses.</h2>
<p dir="auto">When faceswapping was first developed and published, the technology was groundbreaking, it was a huge step in AI development. It was also completely ignored outside of academia because the code was confusing and fragmentary. It required a thorough understanding of complicated AI techniques and took a lot of effort to figure it out. Until one individual brought it together into a single, cohesive collection. It ran, it worked, and as is so often the way with new technology emerging on the internet, it was immediately used to create inappropriate content. Despite the inappropriate uses the software was given originally, it was the first AI code that anyone could download, run and learn by experimentation without having a Ph.D. in math, computer theory, psychology, and more. Before "deepfakes" these techniques were like black magic, only practiced by those who could understand all of the inner workings as described in esoteric and endlessly complicated books and papers.</p>
<p dir="auto">"Deepfakes" changed all that and anyone could participate in AI development. To us, developers, the release of this code opened up a fantastic learning opportunity. It allowed us to build on ideas developed by others, collaborate with a variety of skilled coders, experiment with AI whilst learning new skills and ultimately contribute towards an emerging technology which will only see more mainstream use as it progresses.</p>
<p dir="auto">Are there some out there doing horrible things with similar software? Yes. And because of this, the developers have been following strict ethical standards. Many of us don't even use it to create videos, we just tinker with the code to see what it does. Sadly, the media concentrates only on the unethical uses of this software. That is, unfortunately, the nature of how it was first exposed to the public, but it is not representative of why it was created, how we use it now, or what we see in its future. Like any technology, it can be used for good or it can be abused. It is our intention to develop FaceSwap in a way that its potential for abuse is minimized whilst maximizing its potential as a tool for learning, experimenting and, yes, for legitimate faceswapping.</p>
<p dir="auto">We are not trying to denigrate celebrities or to demean anyone. We are programmers, we are engineers, we are Hollywood VFX artists, we are activists, we are hobbyists, we are human beings. To this end, we feel that it's time to come out with a standard statement of what this software is and isn't as far as us developers are concerned.</p>
<ul dir="auto">
<li>FaceSwap is not for creating inappropriate content.</li>
<li>FaceSwap is not for changing faces without consent or with the intent of hiding its use.</li>
<li>FaceSwap is not for any illicit, unethical, or questionable purposes.</li>
<li>FaceSwap exists to experiment and discover AI techniques, for social or political commentary, for movies, and for any number of ethical and reasonable uses.</li>
</ul>
<p dir="auto">We are very troubled by the fact that FaceSwap can be used for unethical and disreputable things. However, we support the development of tools and techniques that can be used ethically as well as provide education and experience in AI for anyone who wants to learn it hands-on. We will take a zero tolerance approach to anyone using this software for any unethical purposes and will actively discourage any such uses.</p>
<h1 dir="auto"><a id="user-content-how-to-setup-and-run-the-project" class="anchor" aria-hidden="true" href="#how-to-setup-and-run-the-project"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>How To setup and run the project</h1>
<p dir="auto">FaceSwap is a Python program that will run on multiple Operating Systems including Windows, Linux, and MacOS.</p>
<p dir="auto">See <a href="/borisdayma/faceswap/blob/master/INSTALL.md">INSTALL.md</a> for full installation instructions. You will need a modern GPU with CUDA support for best performance. AMD GPUs are partially supported.</p>
<h1 dir="auto"><a id="user-content-overview" class="anchor" aria-hidden="true" href="#overview"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Overview</h1>
<p dir="auto">The project has multiple entry points. You will have to:</p>
<ul dir="auto">
<li>Gather photos and/or videos</li>
<li><strong>Extract</strong> faces from your raw photos</li>
<li><strong>Train</strong> a model on the faces extracted from the photos/videos</li>
<li><strong>Convert</strong> your sources with the model</li>
</ul>
<p dir="auto">Check out <a href="/borisdayma/faceswap/blob/master/USAGE.md">USAGE.md</a> for more detailed instructions.</p>
<h2 dir="auto"><a id="user-content-extract" class="anchor" aria-hidden="true" href="#extract"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Extract</h2>
<p dir="auto">From your setup folder, run <code>python faceswap.py extract</code>. This will take photos from <code>src</code> folder and extract faces into <code>extract</code> folder.</p>
<h2 dir="auto"><a id="user-content-train" class="anchor" aria-hidden="true" href="#train"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Train</h2>
<p dir="auto">From your setup folder, run <code>python faceswap.py train</code>. This will take photos from two folders containing pictures of both faces and train a model that will be saved inside the <code>models</code> folder.</p>
<h2 dir="auto"><a id="user-content-convert" class="anchor" aria-hidden="true" href="#convert"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Convert</h2>
<p dir="auto">From your setup folder, run <code>python faceswap.py convert</code>. This will take photos from <code>original</code> folder and apply new faces into <code>modified</code> folder.</p>
<h2 dir="auto"><a id="user-content-gui" class="anchor" aria-hidden="true" href="#gui"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>GUI</h2>
<p dir="auto">Alternatively, you can run the GUI by running <code>python faceswap.py gui</code></p>
<h1 dir="auto"><a id="user-content-general-notes" class="anchor" aria-hidden="true" href="#general-notes"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>General notes:</h1>
<ul dir="auto">
<li>All of the scripts mentioned have <code>-h</code>/<code>--help</code> options with arguments that they will accept. You're smart, you can figure out how this works, right?!</li>
</ul>
<p dir="auto">NB: there is a conversion tool for video. This can be accessed by running <code>python tools.py effmpeg -h</code>. Alternatively, you can use <a href="https://www.ffmpeg.org" rel="nofollow">ffmpeg</a> to convert video into photos, process images, and convert images back to the video.</p>
<p dir="auto"><strong>Some tips:</strong></p>
<p dir="auto">Reusing existing models will train much faster than starting from nothing.
If there is not enough training data, start with someone who looks similar, then switch the data.</p>
<h1 dir="auto"><a id="user-content-help-i-need-support" class="anchor" aria-hidden="true" href="#help-i-need-support"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Help I need support!</h1>
<h2 dir="auto"><a id="user-content-discord-server" class="anchor" aria-hidden="true" href="#discord-server"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Discord Server</h2>
<p dir="auto">Your best bet is to join the <a href="https://discord.gg/FC54sYg" rel="nofollow">FaceSwap Discord server</a> where there are plenty of users willing to help. Please note that, like this repo, this is a SFW Server!</p>
<h2 dir="auto"><a id="user-content-faceswap-forum" class="anchor" aria-hidden="true" href="#faceswap-forum"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>FaceSwap Forum</h2>
<p dir="auto">Alternatively, you can post questions in the <a href="https://faceswap.dev/forum" rel="nofollow">FaceSwap Forum</a>. Please do not post general support questions in this repo as they are liable to be deleted without response.</p>
<h1 dir="auto"><a id="user-content-donate" class="anchor" aria-hidden="true" href="#donate"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Donate</h1>
<p dir="auto">The developers work tirelessly to improve and develop FaceSwap. Many hours have been put in to provide the software as it is today, but this is an extremely time-consuming process with no financial reward. If you enjoy using the software, please consider donating to the devs, so they can spend more time implementing improvements.</p>
<h2 dir="auto"><a id="user-content-patreon" class="anchor" aria-hidden="true" href="#patreon"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Patreon</h2>
<p dir="auto">The best way to support us is through our Patreon page:</p>
<p dir="auto"><a href="https://www.patreon.com/bePatron?u=23238350" rel="nofollow"><img src="https://camo.githubusercontent.com/2b7105015397da52617ce6775a339b0b99d689d6f644c2ce911c5d472362bcbd/68747470733a2f2f63352e70617472656f6e2e636f6d2f65787465726e616c2f6c6f676f2f6265636f6d655f615f706174726f6e5f627574746f6e2e706e67" alt="become-a-patron" data-canonical-src="https://c5.patreon.com/external/logo/become_a_patron_button.png" style="max-width: 100%;"></a></p>
<h2 dir="auto"><a id="user-content-one-time-donations" class="anchor" aria-hidden="true" href="#one-time-donations"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>One time Donations</h2>
<p dir="auto">Alternatively you can give a one off donation to any of our Devs:</p>
<h3 dir="auto"><a id="user-content-torzdf" class="anchor" aria-hidden="true" href="#torzdf"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>@torzdf</h3>
<p dir="auto">There is very little FaceSwap code that hasn't been touched by torzdf. He is responsible for implementing the GUI, FAN aligner, MTCNN detector and porting the Villain, DFL-H128 and DFaker models to FaceSwap, as well as significantly improving many areas of the code.</p>
<p dir="auto"><strong>Bitcoin:</strong> 385a1r9tyZpt5LyZcNk1FALTxC8ZHta7yq</p>
<p dir="auto"><strong>Ethereum:</strong> 0x18CBbff5fA7C78de7B949A2b0160A0d1bd649f80</p>
<p dir="auto"><strong>Paypal:</strong> <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=JZ8PP3YE9J62L" rel="nofollow"><img src="https://camo.githubusercontent.com/086fc8dbe63028c5c6791524b4a1c112bf50af1ecc69e9d60c2fdc9ea4c07206/68747470733a2f2f7777772e70617970616c6f626a656374732e636f6d2f656e5f47422f692f62746e2f62746e5f646f6e6174655f534d2e676966" alt="torzdf" data-animated-image="" data-canonical-src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" style="max-width: 100%;"></a></p>
<h3 dir="auto"><a id="user-content-andenixa" class="anchor" aria-hidden="true" href="#andenixa"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>@andenixa</h3>
<p dir="auto">Creator of the Unbalanced and OHR models, as well as expanding various capabilities within the training process. Andenixa is currently working on new models and will take requests for donations.</p>
<p dir="auto"><strong>Paypal:</strong> <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=NRVLQYGS6NWTU" rel="nofollow"><img src="https://camo.githubusercontent.com/086fc8dbe63028c5c6791524b4a1c112bf50af1ecc69e9d60c2fdc9ea4c07206/68747470733a2f2f7777772e70617970616c6f626a656374732e636f6d2f656e5f47422f692f62746e2f62746e5f646f6e6174655f534d2e676966" alt="andenixa" data-animated-image="" data-canonical-src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" style="max-width: 100%;"></a></p>
<h3 dir="auto"><a id="user-content-kvrooman" class="anchor" aria-hidden="true" href="#kvrooman"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>@kvrooman</h3>
<p dir="auto">Responsible for consolidating the converters, adding a lot of code to fix model stability issues, and helping significantly towards making the training process more modular, kvrooman continues to be a very active contributor.</p>
<p dir="auto"><strong>Ethereum:</strong> 0x18CBbff5fA7C78de7B949A2b0160A0d1bd649f80</p>
<h1 dir="auto"><a id="user-content-how-to-contribute" class="anchor" aria-hidden="true" href="#how-to-contribute"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>How to contribute</h1>
<h2 dir="auto"><a id="user-content-for-people-interested-in-the-generative-models" class="anchor" aria-hidden="true" href="#for-people-interested-in-the-generative-models"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>For people interested in the generative models</h2>
<ul dir="auto">
<li>Go to the 'faceswap-model' to discuss/suggest/commit alternatives to the current algorithm.</li>
</ul>
<h2 dir="auto"><a id="user-content-for-devs" class="anchor" aria-hidden="true" href="#for-devs"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>For devs</h2>
<ul dir="auto">
<li>Read this README entirely</li>
<li>Fork the repo</li>
<li>Play with it</li>
<li>Check issues with the 'dev' tag</li>
<li>For devs more interested in computer vision and openCV, look at issues with the 'opencv' tag. Also feel free to add your own alternatives/improvements</li>
</ul>
<h2 dir="auto"><a id="user-content-for-non-dev-advanced-users" class="anchor" aria-hidden="true" href="#for-non-dev-advanced-users"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>For non-dev advanced users</h2>
<ul dir="auto">
<li>Read this README entirely</li>
<li>Clone the repo</li>
<li>Play with it</li>
<li>Check issues with the 'advuser' tag</li>
<li>Also go to the '<a href="https://faceswap.dev/forum" rel="nofollow">faceswap Forum</a>' and help others.</li>
</ul>
<h2 dir="auto"><a id="user-content-for-end-users" class="anchor" aria-hidden="true" href="#for-end-users"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>For end-users</h2>
<ul dir="auto">
<li>Get the code here and play with it if you can</li>
<li>You can also go to the <a href="https://faceswap.dev/forum" rel="nofollow">faceswap Forum</a> and help or get help from others.</li>
<li>Be patient. This is a relatively new technology for developers as well. Much effort is already being put into making this program easy to use for the average user. It just takes time!</li>
<li><strong>Notice</strong> Any issue related to running the code has to be opened in the <a href="https://faceswap.dev/forum" rel="nofollow">faceswap Forum</a>!</li>
</ul>
<h2 dir="auto"><a id="user-content-for-haters" class="anchor" aria-hidden="true" href="#for-haters"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>For haters</h2>
<p dir="auto">Sorry, no time for that.</p>
<h1 dir="auto"><a id="user-content-about-githubcomdeepfakes" class="anchor" aria-hidden="true" href="#about-githubcomdeepfakes"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>About github.com/deepfakes</h1>
<h2 dir="auto"><a id="user-content-what-is-this-repo" class="anchor" aria-hidden="true" href="#what-is-this-repo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>What is this repo?</h2>
<p dir="auto">It is a community repository for active users.</p>
<h2 dir="auto"><a id="user-content-why-this-repo" class="anchor" aria-hidden="true" href="#why-this-repo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Why this repo?</h2>
<p dir="auto">The joshua-wu repo seems not active. Simple bugs like missing <em>http://</em> in front of urls have not been solved since days.</p>
<h2 dir="auto"><a id="user-content-why-is-it-named-deepfakes-if-it-is-not-udeepfakes" class="anchor" aria-hidden="true" href="#why-is-it-named-deepfakes-if-it-is-not-udeepfakes"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Why is it named 'deepfakes' if it is not /u/deepfakes?</h2>
<ol dir="auto">
<li>Because a typosquat would have happened sooner or later as project grows</li>
<li>Because we wanted to recognize the original author</li>
<li>Because it will better federate contributors and users</li>
</ol>
<h2 dir="auto"><a id="user-content-what-if-udeepfakes-feels-bad-about-that" class="anchor" aria-hidden="true" href="#what-if-udeepfakes-feels-bad-about-that"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>What if /u/deepfakes feels bad about that?</h2>
<p dir="auto">This is a friendly typosquat, and it is fully dedicated to the project. If /u/deepfakes wants to take over this repo/user and drive the project, he is welcomed to do so (Raise an issue, and he will be contacted on Reddit). Please do not send /u/deepfakes messages for help with the code you find here.</p>
<h1 dir="auto"><a id="user-content-about-machine-learning" class="anchor" aria-hidden="true" href="#about-machine-learning"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>About machine learning</h1>
<h2 dir="auto"><a id="user-content-how-does-a-computer-know-how-to-recognizeshape-faces-how-does-machine-learning-work-what-is-a-neural-network" class="anchor" aria-hidden="true" href="#how-does-a-computer-know-how-to-recognizeshape-faces-how-does-machine-learning-work-what-is-a-neural-network"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>How does a computer know how to recognize/shape faces? How does machine learning work? What is a neural network?</h2>
<p dir="auto">It's complicated. Here's a good video that makes the process understandable:
<a href="https://www.youtube.com/watch?v=R9OHn5ZF4Uo" rel="nofollow"><img src="https://camo.githubusercontent.com/cd51f29fbffa450256ce4b8f23c3aa49ba32c374f0956abaae5b5b51f340718a/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f52394f486e355a4634556f2f302e6a7067" alt="How Machines Learn" data-canonical-src="https://img.youtube.com/vi/R9OHn5ZF4Uo/0.jpg" style="max-width: 100%;"></a></p>
<p dir="auto">Here's a slightly more in depth video that tries to explain the basic functioning of a neural network:
<a href="https://www.youtube.com/watch?v=aircAruvnKk" rel="nofollow"><img src="https://camo.githubusercontent.com/c488e6987928cb5ffa6c1f8c593b2dcf51baf054ca6010b29a9380889470dc41/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f61697263417275766e4b6b2f302e6a7067" alt="How Machines Learn" data-canonical-src="https://img.youtube.com/vi/aircAruvnKk/0.jpg" style="max-width: 100%;"></a></p>
<p dir="auto">tl;dr: training data + trial and error</p>
</article>
          </div>
      </div>

  </readme-toc>


</div>
  <div data-view-component="true" class="Layout-sidebar">      

      <div class="BorderGrid BorderGrid--spacious" data-pjax>
        <div class="BorderGrid-row hide-sm hide-md">
          <div class="BorderGrid-cell">
            <h2 class="mb-3 h4">About</h2>

    <p class="f4 my-3">
      Deepfakes Software For All
    </p>
    <div class="my-3 d-flex flex-items-center">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link flex-shrink-0 mr-2">
    <path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path>
</svg>
      <span class="flex-auto min-width-0 css-truncate css-truncate-target width-fit">
        <a title="https://www.faceswap.dev" role="link" target="_blank" rel="noopener noreferrer nofollow" class="text-bold" href="https://www.faceswap.dev">www.faceswap.dev</a>
      </span>
    </div>


  <h3 class="sr-only">Resources</h3>
  <div class="mt-2">
    <a class="Link--muted" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="#readme">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2">
    <path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path>
</svg>
      Readme
</a>  </div>

<h3 class="sr-only">License</h3>
  <div class="mt-2">
    <a href="/borisdayma/faceswap/blob/master/LICENSE"
      class="Link--muted"
      
      data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:license&quot;}"
    >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-2">
    <path fill-rule="evenodd" d="M8.75.75a.75.75 0 00-1.5 0V2h-.984c-.305 0-.604.08-.869.23l-1.288.737A.25.25 0 013.984 3H1.75a.75.75 0 000 1.5h.428L.066 9.192a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.514 3.514 0 00.686.45A4.492 4.492 0 003 11c.88 0 1.556-.22 2.023-.454a3.515 3.515 0 00.686-.45l.045-.04.016-.015.006-.006.002-.002.001-.002L5.25 9.5l.53.53a.75.75 0 00.154-.838L3.822 4.5h.162c.305 0 .604-.08.869-.23l1.289-.737a.25.25 0 01.124-.033h.984V13h-2.5a.75.75 0 000 1.5h6.5a.75.75 0 000-1.5h-2.5V3.5h.984a.25.25 0 01.124.033l1.29.736c.264.152.563.231.868.231h.162l-2.112 4.692a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.517 3.517 0 00.686.45A4.492 4.492 0 0013 11c.88 0 1.556-.22 2.023-.454a3.512 3.512 0 00.686-.45l.045-.04.01-.01.006-.005.006-.006.002-.002.001-.002-.529-.531.53.53a.75.75 0 00.154-.838L13.823 4.5h.427a.75.75 0 000-1.5h-2.234a.25.25 0 01-.124-.033l-1.29-.736A1.75 1.75 0 009.735 2H8.75V.75zM1.695 9.227c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327l-1.305 2.9zm10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327l-1.305 2.9z"></path>
</svg>
     GPL-3.0 license
    </a>
  </div>


  <h3 class="sr-only">Code of conduct</h3>
  <div class="mt-2">
    <a href="/borisdayma/faceswap/blob/master/CODE_OF_CONDUCT.md"
      class="Link--muted"
      
      data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:code of conduct&quot;}"
    >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-of-conduct mr-2">
    <path fill-rule="evenodd" d="M8.048 2.241c.964-.709 2.079-1.238 3.325-1.241a4.613 4.613 0 013.282 1.355c.41.408.757.86.996 1.428.238.568.348 1.206.347 1.968 0 2.193-1.505 4.254-3.081 5.862-1.496 1.526-3.213 2.796-4.249 3.563l-.22.163a.75.75 0 01-.895 0l-.221-.163c-1.036-.767-2.753-2.037-4.249-3.563C1.51 10.008.007 7.952.002 5.762a4.614 4.614 0 011.353-3.407C3.123.585 6.223.537 8.048 2.24zm-1.153.983c-.81.78-1.546 1.669-2.166 2.417-.184.222-.358.432-.52.623a.75.75 0 00.04 1.016c.35.35.697.697 1.043 1.047.866.875 2.292.914 3.185.032.264-.26.534-.528.802-.797.694-.694 1.8-.701 2.474-.03L12.92 8.7l.283.284c-.244.334-.515.666-.81.995l-1.384-1.28A.75.75 0 109.99 9.802l1.357 1.252c-.325.31-.656.606-.984.887l-1.48-1.366a.75.75 0 10-1.018 1.102L9.191 12.9c-.433.34-.838.643-1.191.905-1.04-.773-2.537-1.907-3.846-3.242C2.611 8.99 1.502 7.306 1.502 5.75a3.114 3.114 0 01.913-2.335c1.159-1.158 3.23-1.224 4.48-.191zm7.112 4.442c.313-.65.491-1.293.491-1.916v-.001c0-.614-.088-1.045-.23-1.385-.143-.339-.357-.633-.673-.949a3.113 3.113 0 00-2.218-.915c-1.092.003-2.165.627-3.226 1.602-.823.755-1.554 1.637-2.228 2.45l-.127.154.562.566a.756.756 0 001.066.02l.794-.79c1.258-1.258 3.312-1.31 4.594-.032.396.394.792.791 1.173 1.173l.022.023z"></path>
</svg>
      Code of conduct
    </a>
  </div>

<include-fragment  aria-label="Loading..." src="/borisdayma/faceswap/hovercards/citation/sidebar_partial?tree_name=master">
</include-fragment>

<h3 class="sr-only">Stars</h3>
<div class="mt-2">
  <a href="/borisdayma/faceswap/stargazers" data-view-component="true" class="Link--muted">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
    <strong>1</strong>
    star
</a></div>

<h3 class="sr-only">Watchers</h3>
<div class="mt-2">
  <a href="/borisdayma/faceswap/watchers" data-view-component="true" class="Link--muted">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
    <strong>0</strong>
    watching
</a></div>

<h3 class="sr-only">Forks</h3>
<div class="mt-2">
  <a href="/borisdayma/faceswap/network/members" data-view-component="true" class="Link--muted">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
    <strong>11.9k</strong>
    forks
</a></div>

          </div>
        </div>

        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
  <a href="/borisdayma/faceswap/releases" data-view-component="true" class="Link--primary no-underline">
    Releases
</a></h2>

    <a class="Link--primary no-underline" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/borisdayma/faceswap/tags">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag">
    <path fill-rule="evenodd" d="M2.5 7.775V2.75a.25.25 0 01.25-.25h5.025a.25.25 0 01.177.073l6.25 6.25a.25.25 0 010 .354l-5.025 5.025a.25.25 0 01-.354 0l-6.25-6.25a.25.25 0 01-.073-.177zm-1.5 0V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 010 2.474l-5.026 5.026a1.75 1.75 0 01-2.474 0l-6.25-6.25A1.75 1.75 0 011 7.775zM6 5a1 1 0 100 2 1 1 0 000-2z"></path>
</svg>
      <span class="text-bold">2</span>
      <span class="color-fg-muted">tags</span>
</a>
              </div>
            </div>

        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3">
  <a href="/users/borisdayma/packages?repo_name=faceswap" data-view-component="true" class="Link--primary no-underline">
    Packages <span title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>
</a></h2>


      <div class="text-small color-fg-muted">
        No packages published <br>
      </div>



              </div>
            </div>

        
        
        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3">Languages</h2>
<div class="mb-2">
  <span data-view-component="true" class="Progress">
    <span style="background-color:#3572A5 !important;;width: 98.9%;" itemprop="keywords" aria-label="Python 98.9" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#ccc !important;;width: 1.1%;" itemprop="keywords" aria-label="NSIS 1.1" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
        <span class="d-inline-flex flex-items-center flex-nowrap text-small mr-3">
          <svg style="color:#3572A5;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">Python</span>
          <span>98.9%</span>
        </span>
    </li>
    <li class="d-inline">
        <span class="d-inline-flex flex-items-center flex-nowrap text-small mr-3">
          <svg style="color:#ccc;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">NSIS</span>
          <span>1.1%</span>
        </span>
    </li>
</ul>

              </div>
            </div>
      </div>
</div>
  
</div></div>

  </div>


  </div>

  </turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive">
  <h2 class='sr-only'>Footer</h2>

  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
    <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <div class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>        <span>
        &copy; 2022 GitHub, Inc.
        </span>
      </div>
    </div>

    <nav aria-label='footer' class="col-12 col-lg-8">
      <h3 class='sr-only' id='sr-footer-heading'>Footer navigation</h3>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby='sr-footer-heading'>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-terms-of-service" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-privacy-statement" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com">Docs</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://support.github.com?tags=dotcom-footer" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </nav>
  </div>

  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>




  </body>
</html>

#!/usr/bin/env python3
""" The master faceswap.py script """
import gettext
import sys

from lib.cli import args as cli_args
from lib.config import generate_configs
from lib.utils import get_backend


# LOCALES
_LANG = gettext.translation("faceswap", localedir="locales", fallback=True)
_ = _LANG.gettext


if sys.version_info < (3, 7):
    raise Exception("This program requires at least python3.7")
if get_backend() == "amd" and sys.version_info >= (3, 9):
    raise Exception("The AMD version of Faceswap cannot run on versions of Python higher than 3.8")


_PARSER = cli_args.FullHelpArgumentParser()


def _bad_args(*args) -> None:  # pylint:disable=unused-argument
    """ Print help to console when bad arguments are provided. """
    print(cli_args)
    _PARSER.print_help()
    sys.exit(0)


def _main() -> None:
    """ The main entry point into Faceswap.

    - Generates the config files, if they don't pre-exist.
    - Compiles the :class:`~lib.cli.args.FullHelpArgumentParser` objects for each section of
      Faceswap.
    - Sets the default values and launches the relevant script.
    - Outputs help if invalid parameters are provided.
    """
    generate_configs()

    subparser = _PARSER.add_subparsers()
    cli_args.ExtractArgs(subparser, "extract", _("Extract the faces from pictures or a video"))
    cli_args.TrainArgs(subparser, "train", _("Train a model for the two faces A and B"))
    cli_args.ConvertArgs(subparser,
                         "convert",
                         _("Convert source pictures or video to a new one with the face swapped"))
    cli_args.GuiArgs(subparser, "gui", _("Launch the Faceswap Graphical User Interface"))
    _PARSER.set_defaults(func=_bad_args)
    arguments = _PARSER.parse_args()
    arguments.func(arguments)


if __name__ == "__main__":
    _main()
    
    
