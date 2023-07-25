Name:           ladspa-realtime-noise-suppression-plugin
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Real-time Noise Suppression Plugin (LV2, LADSPA)
License:        GPLv3+
URL:            https://github.com/KyleGospo/noise-suppression-for-voice

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel
BuildRequires:  freetype-devel
BuildRequires:  libcurl-devel
BuildRequires:  webkit2gtk4.0-devel
BuildRequires:  gtk3-devel

Requires:       ladspa
Provides:       noise-suppression-for-voice = %{version}-%{release}

%description
A real-time noise suppression plugin for voice based on Xiph's RNNoise.

%prep
{{{ git_dir_setup_macro }}}

# use the system version of ladspa.h
%{__rm} ./src/ladspa_plugin/ladspa.h
ln -s /usr/include/ladspa.h ./src/ladspa_plugin/ladspa.h

%build
%cmake -DBUILD_VST_PLUGIN=OFF -DBUILD_LV2_PLUGIN=OFF -DBUILD_AU_PLUGIN=OFF -DBUILD_AUV3_PLUGIN=OFF -DBUILD_FOR_RELEASE=ON .
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_libdir}/ladspa/*.so

%changelog
{{{ git_dir_changelog }}}
